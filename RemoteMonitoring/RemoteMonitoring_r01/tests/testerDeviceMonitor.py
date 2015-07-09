__author__ = 'Index'



import deviceMonitor


def main():



    monitorDevice=deviceMonitor.MonitorDevices('monitorDevice')
    print monitorDevice.deviceConnectivity()







if __name__=='__main__':
    main()
