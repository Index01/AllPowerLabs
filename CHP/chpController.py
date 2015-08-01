#chpController.py

import serial
import glob



# Handle serial connection and reading
class ChpControllLogger():

  def __init__(self, name):
    self.name=name
    self.serialConnection= None


  def serialSetup(self, baud, port, timeout=1):
    self.serialConnection = serial.Serial(baudrate=baud, port=port, timeout=timeout)




  def showPorts(self):
    openPorts = glob.glob('/dev/tty[A-Za-z]*')
    return openPorts


  # Read a specified number of bytes from the stream
  def readSerial(self):
    serialBytes = self.serialConnection.read(250)
    print "reading serial..."
    return serialBytes


  # Read one line \n terminated
  def readSerialLine(self):
    serialLine = self.serialConnection.readline()
    print "reading serial..."
    return serialLine


  def closeSerial(self):
    self.serialConnection.close()






