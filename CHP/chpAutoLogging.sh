#!/bin/bash


clear

logFile=./chpBashScriptLogFile.log
echo "[*] CHP logging start"

echo "[+] next entry: " >> $logFile
python /home/pi/CHP/monitor/chpMonitorMain.py >> $logFile 2>&1
echo " " >> $logFile

echo "[+] Finished"


