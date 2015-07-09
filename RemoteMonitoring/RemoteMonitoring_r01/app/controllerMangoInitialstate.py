# -*- coding: utf-8 -*-
"""
Created on Tue Jun 02 16:20:33 2015

@author: Index

Mango and Initial state controller implementation. Get data from Mango, send it to 
Initial State, additionally expose the option to call and receive the current data 
state from Mango object. Checking data state will allow subsequent implementations
to determine whether the machine is offline or otherwise generating bogus data. 

"""

import apiConnector as api
from ISStreamer.Streamer import Streamer
from ConfigParser import SafeConfigParser


#TODO: Add an ini file for loading initial endpoint and authentication information
class MangoInitialStateController():


    
    def __init__(self, name):
        self.name=name

        '''We will be using an .ini file for holding auth and instance info. setup here'''
        self.parser = SafeConfigParser()
        self.parser.read('RemoteMonitoringConfigs.ini')

        self.mangoApiUrl=self.parser.get('MangoApi', 'apiEndpoint')
        self.mangoConnection=api.Connection("mangoConnection", endpointUrl=self.mangoApiUrl)
        self.currentAuthStatus=None
        self.__auth__()



    '''Auth only'''
    def __auth__(self):
        mangoUserName=self.parser.get('MangoAuth','uname')
        mangoPass=self.parser.get('MangoAuth','pass')
        mangoAuthUrl=self.parser.get('MangoAuth', 'authEndpoint')
        authStatusCode=self.mangoConnection.authConnect(authenticationUrl=mangoAuthUrl, username=mangoUserName, password=mangoPass)
        self.currentAuthStatus=authStatusCode
        
        return



    '''Public method for accessing authentication'''
    def renewAuth(self):
        self.__auth__()
        authCheck=self.authStatus()

        return authCheck



    '''Check our Mango authentication status'''
    def authStatus(self):

        if self.currentAuthStatus is None:
            print "[-] Failed to authenticate to endpoint at controller __init__"
            return None
        elif self.currentAuthStatus==200:
            return self.currentAuthStatus
        else:
            return "[-] You got a problem, yo: %s" % self.currentAuthStatus



    '''Return the raw data dictionary pulled from the device to the calling function'''    
    def returnDataState(self, deviceNameValue=None):
        if deviceNameValue is None:
            apiDataSubset=self.mangoConnection.getData()
        else:    
            apiDataSubset=self.mangoConnection.getDataMemberSubset('deviceName', deviceNameValue)   
    #       print "API data subset: \n %s" % apiDataSubset

        return apiDataSubset
    
    
        
    '''The moment we have all been waiting for. Call this function to do the magic'''
    def logDataToIS(self, deviceNameValue=None, bucketName=None):
        self.mangoConnection.getData()    #Make sure we have the most current data available

        apiDataSubset=self.mangoConnection.getDataMemberSubset('deviceName', deviceNameValue)
        dataSetKeyVal={}
        key=self.parser.get('InitialStateAuth','accessKey')


        try:
            streamer = Streamer(bucket_name=bucketName, bucket_key=deviceNameValue, buffer_size=100, access_key=key, debug_level=1)
        except Exception, e:
            print "[-] Exception occurred while attempting Initial State connection. Except: %s" % e

        for hashRow in apiDataSubset:
            dataSetKeyVal[hashRow['name']]=hashRow.get('renderedValue')
            streamer.log(hashRow['name'], hashRow.get('renderedValue'))

    #    Streamer.log()
    #    Streamer.log_object()
        try:
            streamer.flush()    # flush the stream to ensure optimal buffer and consumption experience
            streamer.close()    # cleanup the stream and ensure logs are flushed
        except Exception, e:
            print "[-] Exception occurred while logging data to Initial State. Except: %s " % e


        return dataSetKeyVal.items()
