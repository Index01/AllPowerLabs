__author__ = 'Index'

'''
testerControllerMangoInitialState.py
Created on Fri Jun 05 10:49:45 2015

@author: Index

Mango and Initial State controller implementation tester. This tester doest not use unittest, instead if just prints all returned values to help with debugging.
'''

import controllerMangoInitialstate

def main():
    print "[*] OBJ INSTANT"
    mangoInitialStateController=controllerMangoInitialstate.MangoInitialStateController('mangoInitialStateController')
    print "[*] AUTH STATUS:"
    print mangoInitialStateController.authStatus()
    print "[*] RETURN DATA STATE:"
    print mangoInitialStateController.returnDataState()
    print "[*] RETURN DATA STATE WITH ARGV:"
    print mangoInitialStateController.returnDataState('pp1039')
    print "[*] LOG TO IS:"
    print mangoInitialStateController.logDataToIS('pp1039', 'Power Pallet 1039')


if __name__=='__main__':
    main()
