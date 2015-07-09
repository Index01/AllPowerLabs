#chpNewDataLogger.py
'''
  This code was written with the quickness, iterations will be necessary. 
  Objectives: Grab data from the serial ports in /dev/, determine whether it
  is a complete dataset, if yes form it into a transportable datatype and 
  hand it off to a function which will deal with persistent storage. If the
  dataset is incomplete forget about it like a 3 dollar bill and get new data.
'''

import chpController
import shlex
import chpDataWrite
import datetime


def getData(chpController):
  tcu = chpController 
  serialBytesLine = tcu.readSerialLine()

#  shlexBytes = shlex.shlex(serialBytes)
  shlexBytes = shlex.shlex(serialBytesLine)
  shlexBytes.wordchars += '.'  
  shlexBytes.whitespace += ','
  shlexBytes.whitespace += ':'
  shlexBytes.whitespace += '{ }'

  shlexList = []
  
  for i in shlexBytes:
    shlexList.append(i)

  return shlexList



def localizeData(chpController):
  finalListVals = {}	
  controlUnit = chpController
  finalListVals = stripAndCheck(controlUnit)

 
  return finalListVals


# Check that the data seems to be what we are looking for, if not go back and get new data.
def stripAndCheck(chpController):
  shlexList = []
  cleanList = []
  outList = []
  dictVals = []

  tcu = chpController
  shlexList = getData(tcu)

  for c in range(7):
    for i, e in enumerate(shlexList): 
      if str(e) == str(c):
        try:
          cleanList.append(c)
          cleanList.append(shlexList[i+1])
        except IndexError as e:
          print "[-] index error %s" % e
          # Did you mean, recursion...?
          stripAndCheck(tcu)


  #TODO: Currently only checking that the data is the appropriate size, not looking at data validity at this point. Implement data validation and integrity checks.
  if len(cleanList) == 12:
    #TODO: sort out the recursive call and returns. filtering none types for now
    outList = cleanList[:]
    dictVals = listToDict(outList)
    print dictVals
    return dictVals

  else:
    # Did you mean, recursion...?
    stripAndCheck(tcu)



#TODO: have this function return a dictionary and handle the persistent layer elsewhere. currently the recursion model does not like returning a consistent datatype.
def listToDict(listVals):
  listVals = listVals

  dictVals = dict(zip(listVals[0::2], listVals[1::2]))
  dictVals['Datetime'] = datetime.datetime.now()

  DataWriter = chpDataWrite.ChpWriter('DataWriter') 
  DataWriter.writeToCsv(dictVals)

  return dictVals



def pcu():
  # process control unit
  ecu = chpController.ChpControllLogger('ecu')
#  print ecu.showPorts()



def main():
  
  # Temperature control unit
  tcu = chpController.ChpControllLogger('tcu')
#  print tcu.showPorts()
#  tcu.serialSetup(9600, '/dev/ttyAMA0')
#  tcu.serialSetup(9600, '/dev/ttyprintk')
  tcu.serialSetup(9600, '/dev/ttyACM0')
  localListVals = localizeData(tcu)



if __name__=='__main__':
  main()
