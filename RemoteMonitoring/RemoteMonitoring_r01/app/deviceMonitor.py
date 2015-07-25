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
        self.connectedDevices=[]
        self.connectedDevices=map(lambda dRow : dRow['status'] if dRow['deviceName'] in self.connectedDevices else dRow['deviceName'], self.modelState)
        self.connectedDevices=list(set(self.connectedDevices))
       # print self.connectedDevices
        return
            
            
        
    '''Check that the devices are connected, return a dictionary with deviceName:boolean'''
    def deviceConnectivity(self):
        self.__devices__()
        dDeviceConnected={}

        for device in self.connectedDevices:
            for dRow in self.modelState:
                if dRow['deviceName']==device:
                    if dRow['status']!='ok':
                        dDeviceConnected[device]=False
                        break
                    else:
                        dDeviceConnected[device]=True
                        break
                else:
                    pass

        return dDeviceConnected



    '''Return a dictionary of currently running devices, {deviceName:boolean(running)}'''
    def deviceRunning(self):

        connectedDevices=self.deviceConnectivity()
        dEngineSpeed={}
        dRunningState={}

        for connectedDeviceName in connectedDevices.keys():
            if connectedDevices.get(connectedDeviceName)==True:
                for elem in self.modelState:
                    if elem.get('deviceName')==connectedDeviceName:
                        if elem.get('name')=='Engine speed':
                            dEngineSpeed[connectedDeviceName]=elem.get('value')
                        else:
                            pass
                    else:
                        pass
            else:
                pass

        # Filter values for machines which are not running, append true for those which are running
        for machine, speed in dEngineSpeed.items():
            if int(speed) != 0:
                print machine,speed
                dRunningState[machine]=True


        return dRunningState



    #TODO: A function to inform the scheduler of the polling interval which should be used.
    '''Return a dictionary of devices with the interval at which they should be polled in seconds. {deviceName:int}'''
    def devicePollInterval(self):
        dPollInterval={}    # This should probably be a tuple. dictionary for now

        dRunStateStatus=self.deviceRunning()
        for machine, runState in dRunStateStatus:
            if runState==True:
                dPollInterval[machine]=10    # 10second polling interval for connected running devices
            else:
                dPollInterval[machine]=30    # 30second polling interval for connected non-running devices


        return dPollInterval


