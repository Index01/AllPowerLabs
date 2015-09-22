__author__ = 'Index'

'''
controllerScheduler.py
Created on Fri Jun 05 13:23:15 2015

@author: Index

Scheduler for controller. We need polling to occur at a consistent interval
as well as a few logic checks for confirming device connectivity. We will use a timer for
checking device connectivity, data will only be transmitted if devices are connected.
'''

import sched
import time
import controllerMangoInitialstate
import deviceMonitor

#TODO: Sort this shit out
class Scheduler():


    '''Setup some timer and scheduler stuff'''
    def setup(self):

        scheduler=sched.scheduler(time.time, time.sleep)
        controllerInstance=controllerMangoInitialstate.MangoInitialStateController("controllerInstance")
        monitor=deviceMonitor.MonitorDevices("monitor")




    '''Check device connectivity, change timing interval relative to device responsiveness'''
    def heartBeat(monitor):
        maxInterval=350             # The maximum time interval we will use in seconds.
        lastPollSuccess=0           # Number of seconds since last successful response
        deviceStatus=monitor.deviceConnectivity()



        # Here we are really just checking for connectivity, not polling



    '''Update the endpoint'''
    def makeTheMagicHappen(controllerInstance, dictDevices):
        dictDevice=dictDevices
        deviceList=[]

        for key in dictDevice.keys():
            deviceList.append(key)


        controllerInstance.logDataToIS()




    '''End monitoring'''
    def halt(self):
        return

#TODO: Sort this shit out, too.
class Task():

    def __init__(self, name, object):
        self.name=name
        self.object=object

    def executeTask(self, func, *args):
        retVal=func(*args)


#        retVal=self.object*func(args)
#        assert isinstance(retVal.fun, object)
       # retVal.fun

        return retVal

    def getTaskObject(self):
        return self.object



def main():
    task=Task('task',controllerMangoInitialstate.MangoInitialStateController('mangoInitialStateController') )
    myNewTask=task.executeTask(func=controllerMangoInitialstate.MangoInitialStateController.authStatus, args=task.getTaskObject(task))

    print myNewTask

if __name__=='__main__':
    main()