__author__ = 'Index'



import deviceMonitor
import timeit


def main():


    monitorDevice=deviceMonitor.MonitorDevices('monitorDevice')



    print '\n'
    print "Start conn test"
    deviceConn=timeit.timeit('MonitorDevices.deviceConnectivity', setup='from deviceMonitor import MonitorDevices', number=1000)
    print 'Time to execute dev conn: %s ' % deviceConn
    print monitorDevice.deviceConnectivity()

    print '\n'

    print "Start devRunState test"
    deviceRunning=timeit.timeit('MonitorDevices.deviceRunning', setup='from deviceMonitor import MonitorDevices', number=1000)
    print 'Time to execute dev run state: %s ' % deviceRunning
    print monitorDevice.deviceRunning()

    print '\n'

    devicePollInterval=timeit.timeit('MonitorDevices.devicePollInterval', setup='from deviceMonitor import MonitorDevices', number=1000)
    print 'Time to execute dev poll interval: %s ' % devicePollInterval
    print monitorDevice.devicePollInterval()



if __name__=='__main__':
    main()
