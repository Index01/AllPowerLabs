# -*- coding: utf-8 -*-
"""
 This is going to do some stuff. Currently it does nothing. Just getting some ideas down
"""

import json
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
            localData==self.session.get(self.endpointUrl)
        except Exception, e:
            print e
            
        
        self.currentData=localData


    
    ''' If you need to auth at a different url first, setup here. '''    
    def authConnect(self, authenticationUrl=None):
        authenticationUrl=authenticationUrl


        
    ''' Return the complete response to the calling object as a list '''
    def getData(self):
        Connection.__localizeData__()

        
        return self.currentData
    
    
    ''' Return only the available keys from the response object '''
#    def getDataMemberKeys(self):
            
            

    ''' Return a subset of the response object which match a key:val pair '''
#    def getDataMemberSubset(self):


