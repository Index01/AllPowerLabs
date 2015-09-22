# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:09:11 2015

@author: Index

mangoConnectionTester.py
"""
import apiConnector as api

def main():
    
    mangoConnection=api.Connection("mangoConnection", endpointUrl='http://10.1.10.242/rest/v1/realtime.json?limit=100')
    mangoConnection.authConnect(authenticationUrl='http://10.1.10.242/login.htm',username='admin',password='admin')
    apiData=mangoConnection.getData()
#    print "API response data: \n %s" % apiData
    apiDataSubset=mangoConnection.getDataMemberSubset('deviceName', 'pp717')   
    print "API data subset: \n %s" % apiDataSubset
    
    
    
if __name__=="__main__":
    main()