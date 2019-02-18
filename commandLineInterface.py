import TdposInterface
import googleSheetsPoster
import globals

class commandLineInterface:
    @staticmethod
    def obtainPrintJob():
        while True:
            userEmail = input('type an email ')
            try:
                printJobDict = (TdposInterface.TdposMiner.search(self, globals.driver, userEmail))
                break
            except Exception as e:
                print(e)
                print('Email not found. Restarting search')
        print('found job:') 
        print(printJobDict)
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

if __name__ == '__main__':
    self = 'self'
    #opens the instance of chrome on startup. Initializes the global variable so every function talks to the same chrome client
    globals.driver = TdposInterface.TdposMiner.initializeListener(self)
    while True:
        commandLineInterface.obtainPrintJob()