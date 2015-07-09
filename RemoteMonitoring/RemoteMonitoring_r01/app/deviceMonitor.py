# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 17:41:51 2015

@author: Index

Implement the controller and monitor the device status, if the device is not connected
or has started sending bogus data, decrement the scheduler timing interval. If the 
device continues to be non-responsive, tell the scheduler to give up on life. 

"""
import apiConnector as api
import controllerMangoInitialstate as controller

class MonitorDevices():
    
    
    
    '''Setup all dat good shit'''
    def __init__(self, name):    
        self.name=name
        self.connectedDevices=[]
    
        self.monitorApiConnection=controller.MangoInitialStateController("monitorApiConnection")
        self.modelState=None

        
        
    '''Just list the devices by name which currently have profiles, add them to a list and return'''
    def __devices__(self):
        self.modelState=self.monitorApiConnection.returnDataState()
                
        for dRow in self.modelState:
            if dRow['deviceName']:
                if dRow['deviceName'] in self.connectedDevices:
                    pass
                else:
                    self.connectedDevices.append(dRow['deviceName'])
            else:
                pass

        for elem in self.connectedDevices:
            print elem

        return            
            
            
        
    '''Check that the devices are connected, return a dictionary with deviceName:boolean'''
    def deviceConnectivity(self):
        self.__devices__()
        dDeviceConnected={}

        for device in self.connectedDevices:
            for dRow in self.modelState:
                if dRow['deviceName']==device:
                    if dRow['status']=='Point value may not be reliable':
                         dDeviceConnected[device]=False
                    else:
                         dDeviceConnected[device]=True
                else:
                    pass

        return dDeviceConnected

