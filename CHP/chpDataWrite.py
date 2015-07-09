#chpDataWrite.py

import pandas
import datetime
import os.path

# Just getting started here. I would like to do this with pandas primarily, 
# eventually it should do some graphing or etc, for now just csv. 

class ChpWriter():
  

  def __init__(self, name):
    self = self
    self.name = name
    self.date = datetime.date.today()
    exitstingFrame = None
    self.filePath = None

  def existingDataFrame(self):
    self.filePath = str(self.date) + "_chpLog.csv"
    fileExists = os.path.exists(self.filePath)
    
    if fileExists:
      print "[+] Found existing log file for date %s" % self.date
      return True 
    else:
      print "[-] No existing log file for date %s" % self.date
      return False 


  def writeToCsv(self, dict):
    dictionaryValues = dict
    appendToFrame = self.existingDataFrame()
    oldFrame = None
    newFrame = None
    

    #TODO: Do something with this list. maybe final validity check. maybe remove.
    listOfVals = []

    for val in dictionaryValues.values():
      listOfVals.append(val)

    if appendToFrame:      
      #TODO: IDK what is up with this Index[0] stuff, need to increment
      newFrame = pandas.DataFrame(dictionaryValues, index=[0])
      print "[+] Appending to existing file" 
      with open(self.filePath, 'a') as oldFrame:
        newFrame.to_csv(oldFrame, header=False)
   
    else:
      newFrame = pandas.DataFrame(dictionaryValues, index=[0])    
      print "[+] Created newFrame, writing to file"
      newFrame.to_csv(self.filePath, mode='a')


