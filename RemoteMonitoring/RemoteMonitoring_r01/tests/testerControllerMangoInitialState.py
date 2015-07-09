__author__ = 'Index'

'''
testerControllerMangoInitialState.py
Created on Fri Jun 05 10:49:45 2015

@author: Index

Mango and Initial State controller implementation tester.
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
    print mangoInitialStateController.returnDataState('pp717')
    print "[*] LOG TO IS:"
    print mangoInitialStateController.logDataToIS('pp717', 'Power Pallet 717')


if __name__=='__main__':
    main()
