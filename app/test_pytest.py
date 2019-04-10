import commandLineInterface    # The code to test

printSelection = [0,1,2]
printJobs = ['samplejob1', 'samplejob2', 'samplejob3', 'samplejob4']
'''
need to setup a mock input to use this
def test_JobSelection():
    assert commandLineInterface.commandLineInterface.selectPrintJobs(self, printSelection) == [1,2,3]
'''

def test_enterPrintJob():
    assert commandLineInterface.commandLineInterface.enterPrintJob('self', printSelection, printJobs) == ['samplejob1', 'samplejob2', 'samplejob3']


