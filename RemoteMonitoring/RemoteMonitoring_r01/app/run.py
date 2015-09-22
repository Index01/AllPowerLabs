__author__ = 'Index'

''' This is the main run file for APL remote monitoring application. No commandline args are supported at this time,
    just python run.py and all the monitoring, connecting and scheduling will be handled. Make sure there is an
    .ini file with auth information.'''

#import time
import scheduler
import controllerMangoInitialstate
import deviceMonitor


def main():


    MyScheduleManager=scheduler.scheduleManager('myScheduleManager')
    MISController=controllerMangoInitialstate.MangoInitialStateController("MISController")
    MyDeviceMonitor=deviceMonitor.MonitorDevices('MyDeviceMonitor')

    def wait():
        def wrappedWait():
            pass
        return wrappedWait()



    def scheduleViableMachine():
        dRunningMachines=MyDeviceMonitor.devicePollInterval()
        if len(dRunningMachines)==0:
            MyScheduleManager.addTask(interval=60, func=wait)    # If there are no running machines, slow down the scheduling and polling
            return
        else:
            #TODO: Confirm that there are no scheduling conflicts when multiple machines are running
            for machine, pollTime in dRunningMachines.items():
                #MyScheduleManager.addTask(MISController.logDataToIS, 'pp1010')
                #MyScheduleManager.addTask(interval=pollTime, func=MISController.logDataToIS, arg=str(machine))
                MyScheduleManager.addTask(pollTime, MISController.logDataToIS, machine)

        return



    while True:
        #print "pre-run queue: %s" % MyScheduleManager.checkQueue()
        scheduleViableMachine()

        print "[+] Runnin dat task"
        #print time.time()
        MyScheduleManager.run()

        #print "post-run queue: %s " % MyScheduleManager.checkQueue()
        #print "[+] Been got dat task runned!"



if __name__=='__main__':
    main()











