__author__ = 'Index'

import unittest
import controllerMangoInitialstate

class MangoInitialStateControllerTest(unittest.TestCase):

    def setUp(self):
        print "[+] Creating new Mango Initial State Controller"
        self.MangoInitialStateControllerTesterInstance=controllerMangoInitialstate.MangoInitialStateController("MangoInitialStateControllerTesterInstance")



    def tearDown(self):
        print "[+] Destroy Mango Initial State instance"
        self.MangoInitialStateControllerTesterInstance=None



    def test_renew_auth(self):
        print "[*] Running test_renew_auth"
        self.failUnlessEqual(self.MangoInitialStateControllerTesterInstance.renewAuth(), 200)



    def test_auth_status(self):
        print "[*] Running test_auth_status"
        self.failUnlessEqual(self.MangoInitialStateControllerTesterInstance.authStatus(), 200)



    def test_return_data_state(self):
        print "[*] Running test_return_data_state"
        self.failUnless(self.MangoInitialStateControllerTesterInstance.returnDataState(), list)



    def test_log_data_to_is(self):
        print "[*] Running test_log_data_to_is"
        self.failUnless(self.MangoInitialStateControllerTesterInstance.logDataToIS('pp1010'),dict)



if __name__ == '__main__':
    unittest.main()
