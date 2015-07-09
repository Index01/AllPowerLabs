# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:09:11 2015

@author: Index
apiConnector.py
"""


import sys
#import json
import requests

class Connection():

    
    ''' Initialize connection at instantiation. Must provide url for your final destination '''
    def __init__(self, name, endpointUrl=None):
        self.name=name
        self.endpointUrl=endpointUrl
        self.currentData=None

        self.session=requests.Session()



    ''' localize data to connection object '''
    def __localizeData__(self):
        localData=None

        try:
            localData=self.session.get(self.endpointUrl)
            if localData.status_code==200:
                print "[+] Data localization success"
            else:
                print "[-] Not authenticated during __localizeData__ operation %s " % localData.status_code
        except requests.exceptions.RequestException as e:
            print "[-] Failed to connect during data localization. Exception: %s" % e
            sys.exit(1)
                    
        self.currentData=localData.json()
    
        
    
    ''' If you need to auth at a different url first, setup here. '''    
    def authConnect(self, authenticationUrl=None, username=None, password=None):
        authenticationUrl=authenticationUrl
        data={"username":username,"password": password}

        try:
            authResponse=self.session.post(authenticationUrl, data=data)
        except requests.exceptions.RequestException as e:
            print "[-] Failed to connect during authentication. Exception: %s" % e
            sys.exit(1)

        authStatusCode = authResponse.status_code
        if authStatusCode != 200:
            print "[-] Failed Authentication, code: %s" % authStatusCode
        else:
            print "[+] Auth Success!"
            
            
        return authStatusCode
        

        
    ''' Return the complete response to the calling object as a list '''
    def getData(self):
        self.__localizeData__()
        data = self.currentData
        
        return data


    
    ''' Return a subset of the response object which match a key:val pair '''
    def getDataMemberSubset(self, key, val):
        subsetList=[]
        print "[+] Returning data for key: %s and val: %s pair" % (key, val)
        for hashLine in self.currentData:
            if hashLine[key]==str(val):
                subsetList.append(hashLine)
            else:
                pass


        return subsetList        


    
#    ''' Return only the available keys from the response object '''
#    def getDataMemberKeys(self):
#            
#            
#            
##        return dataMemeberKeys    
        
        