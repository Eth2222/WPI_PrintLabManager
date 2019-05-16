from unittest.mock import patch
from unittest import TestCase

import commandLineInterface    # The code to test

printSelection = [0,1,2]
badPrintSelection = [1,'cow',3]
printJobs = ['samplejob1', 'samplejob2', 'samplejob3', 'samplejob4']
'''
need to setup a mock input to use this
def test_JobSelection():
    assert commandLineInterface.commandLineInterface.selectPrintJobs(self, printSelection) == [1,2,3]
'''
def test_enterPrintJob(self):
    assert self.commandLineInterface.commandLineInterface.enterPrintJob(printSelection, printJobs) == ['samplejob1', 'samplejob2', 'samplejob3']
def test_selectPrintJobs(self):
    @patch('commandLineInterface.commandLineInterface.selectPrintJobs.get_input', return_value=[1,2,3])
    assert self.commandLineInterface.commandLineInterface.selectPrintJobs(printJobs)== [1,2,3]
