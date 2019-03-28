import TdposInterface
import googleSheetsPoster
import globals
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

from examples import custom_style_2

class commandLineInterface:
    @staticmethod
    def obtainPrintJob():
        while True:
            userEmail = input('type an email ')
            try:
                jobMatchList = (TdposInterface.TdposMiner.search(self, globals.driver, userEmail))
                break
            except Exception as e:
                print(e)
                print('Email not found. Restarting search') 
        #the -1 is so that the actual list item is selected because they are displayed as 1 greater than the actual index
        printSelectionNumber = int(input("please type the number next to the print you would like to queue "))-1
        try:
            printJobDict = ' '
            printJobDict = TdposInterface.TdposMiner.parser(self, jobMatchList[printSelectionNumber])
        except Exception as e1:
            print(e1)

        print('this is the parsed data ', printJobDict)
        submit = input('would you like to submit to the queue? Y/N ')
        if (submit==('Y'or'y')):
            #take unknown data as text input, then add to the dict and pass to the form method
            #color, name, class
            #call google form submission method
            print('!!!Only works for PLA Prints!!!')
            print('additional information needed')
            printJobDict['customerName'] = input('please type customer name ')
            printJobDict['colorPref'] = input('color preference ')
            googleSheetsPoster.googleSheetsPoster.fillForm(printJobDict)
            return
        else:
            print('restarting search function')
            #call search function from the top
            commandLineInterface.obtainPrintJob()

question = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
    }
]


if __name__ == '__main__':
    self = 'self'
    #opens the instance of chrome on startup. Initializes the global variable so every function talks to the same chrome client
    globals.driver = TdposInterface.TdposMiner.initializeListener(self)
    while True:
        commandLineInterface.obtainPrintJob()
        print(prompt(question, style=custom_style_2))