CHP data acquisition is a new project and is subject to significant change. 

Currently we are looking for serial over the /dev/ ports and checking that data against a narrow interpretation of valid data then logging those streams to some sort of persistent storage, at the moment a .csv. Future development may include graphing, located in the DataWrite object and connecting to serial through the chpController class. Everything is tied together with the chpMonitorMain.
 

To run the modules:

 ~/CHP/monitor $ sudo python chpMonitorMain.py
 or run the .sh script which executes the python and logs errors 

simple stuff. 
