#!/bin/bash

# This script will be run in cron to check that necessary services are running for remote monitoring.

mangoStart () {
  echo "[*] Starting Mango"
  cd /opt/mango/bin/
  #$(./ma.sh start)
}

remoteMonStart () {
  echo "[*] Starting ReMon Python scripts" 
  cd /opt/RemoteMonitoring_r01/app/
  python ./run.py
}

mangoFunc () {
  mangoStart &
  mangoFuncId=$!
}

quit () {
  kill $mangoFuncId >/dev/null 2>&1
  exit
}


# Stuff starts happening down here. 
mangoStatus=$(pgrep ma-start.sh)
pythonStatus=$(pgrep python)
regex=^-?[0-9]+$

# Check that mango services are running, if not start them
[[ "$mangoStatus" =~ $regex ]] && echo "[+] Mango already running" || mangoFunc

# Check that python scripts for sending from Mango to Initial State are running, if not start.
[[ "$pythonStatus" =~ $regex ]] && echo "[+] ReMon Python scripts already running" || remoteMonStart

echo "Done."
quit
