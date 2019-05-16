import TdposInterface
import googleSheetsPoster
import globals
#from PyInquirer import style_from_dict, Token, prompt
#from PyInquirer import Validator, ValidationError
import re
#import userPermissionsChecker
from examples import custom_style_2

class commandLineInterface:
    def obtainPrintJob(self, driver):
        while True:
            userEmail = input('type an email ')
            try:
                jobMatchList = (TdposInterface.TdposMiner.search(self, globals.driver, userEmail))
                if len(jobMatchList) != 0:
                    return jobMatchList
                else:
                    raise Exception('empty list error')
                for i in jobMatchList:
                 #Where the job matches are printed in a selectable list form. 
                 #added the +1 to get rid of the zero in the list
                    print((jobMatchList.index(i)+1)," )  ",i)  
                
            except Exception as e:
                print(e)
                print('Email not found. Restarting search') 

    def selectPrintJobs(self, printJobs):
        printSelection = input('select prints ')
        tempList = re.findall(r'\d*', printSelection)
        for i in tempList:
            if i.isdigit() == True:
                int(i)
            else:
                tempList.remove(i)
        parsedSelection = tempList
        return(parsedSelection)

    def print_details(self, parsedPrint):
        parsedPrint.update({'colorPref':input("Color: ")})
        ##insert material information here later
        return parsedPrint  

    def enterPrintJob(self, selection, printJobs, customerName):
        while True:
        #trying to correlate the number selection with a number in the printjobs list
            selected_prints_list = []
            for i in selection:
                #convert the input to int
                i = int(i)
                #print(selection.index(i))
                parsedPrint = TdposInterface.TdposMiner.parser(self, printJobs[i-1])
                print(parsedPrint.get('printName'))
                parsedPrint.update({'customerName':customerName})
                complete_print_info = commandLineInterface.print_details(self, parsedPrint)
                selected_prints_list.append(complete_print_info)
                #now we need to add the extra information to the print. I will write a hepler method for this 
                # not sure why this is here selected_prints_list = commandLineInterface.print_details(self, parsedPrint)
            return(selected_prints_list)
 
'''
    @staticmethod
    def obtainPrintJob():
        while True:
            userEmail = input('type an email ')
            try:
                jobMatchList = (TdposInterface.TdposMiner.search(self, globals.driver, userEmail))
                if not jobMatchList:
                    raise Exception('empty list error')
                for i in jobMatchList:
                 #Where the job matches are printed in a selectable list form. 
                 #added the +1 to get rid of the zero in the list
                    print((jobMatchList.index(i)+1)," )  ",i)  
                break
            except Exception as e:
                print(e)
                print('Email not found. Restarting search') 

        #the -1 is so that the actual list item is selected because they are displayed as 1 greater than the actual index
        printSelectionNumber = int(input("please type the numbers next to the prints you would like to queue "))
        try:
            enterPrintJobDict(self, print)
            printJobDict = TdposInterface.TdposMiner.parser(self, jobMatchList[printSelectionNumber-1])
        except Exception as e1:
            print(e1)
            print('error raised, select an available print')

    def printSelectionParser(self, string):
        printSelections = re.findall(r'\d*')
        #return printSelections which will be a list of all digits
        print('print selections: ', printSelections)
        return printSelections

                
    def enterPrintJob(self, printJobDictList):
        customerName = input('please type customer name ')
        for printJobDict in printJobDictList:

        #print('this is the parsed data ', TdposInterface.TdposMiner.printDict(printJobDict))
        #submit = input('would you like to submit to the queue? Y/N ')
        #if (submit==('Y'or'y')):
            #take unknown data as text input, then add to the dict and pass to the form method
            #color, name, class
            #call google form submission method
            print('!!!Only works for PLA Prints!!!')
            print('additional information needed')
            printJobDict['customerName'] = customerName
            printJobDict['colorPref'] = input('color preference ')
            googleSheetsPoster.googleSheetsPoster.fillForm(printJobDict)
        return

        else:
            print('restarting search function')
            #call search function from the top
            commandLineInterface.obtainPrintJob()

the beginning of a pyinquirer integration
question = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
    }
]
'''

if __name__ == '__main__':
    self = 'self'
    #opens the instance of chrome on startup. Initializes the global variable so every function talks to the same chrome client
    globals.driver = TdposInterface.TdposMiner.initializeListener(self)
    while True:
        #print(prompt(question, style=custom_style_2))
        printJobs = commandLineInterface.obtainPrintJob(self, globals.driver)
        for i in printJobs:
            print((printJobs.index(i)+1)," )  ",i)  
        selection = commandLineInterface.selectPrintJobs(self, printJobs)
        print(selection)
        #user validation check here
        customerName = input('Customer Name: ')
        selected_prints_list = commandLineInterface.enterPrintJob(self, selection, printJobs, customerName)
        for i in selected_prints_list:
            googleSheetsPoster.googleSheetsPoster.fillForm(i)
