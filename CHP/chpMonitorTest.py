# chpMonitorTest.py

import chpController


#TODO: unit tests for modules and classes. needs completion.
def main():
  

  # Temperature control unit
  tcu = chpController.ChpControllLogger('tcu')
  tcu.serialSetup(9600, '/dev/ttyACM0')
  
  serialBytes = tcu.readSerial()
  serialBytesLine = tcu.readSerialLine()


  print "serial Bytes: "
  print serialBytes
  print "line bytes: "
  print serialBytesLine



  # Engine control unit - not really built out yet
  ecu = chpController.ChpControllLogger('ecu')
  print ecu.showPorts()




if __name__=='__main__':
  main()
