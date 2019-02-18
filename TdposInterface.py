from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import printJob
import re
import commandLineInterface
import tdposUserCredentials
#from selenium.webdriver.support.ui import WebDriverWait
import globals


class TdposMiner() :
    
    def initializeListener(self):
        driver = webdriver.Chrome()
        #login procedure. Will need to remove username and passwords and make them gui inputs in future
        driver.get('https://cloud.3dprinteros.com/printing/')
        driver.find_element_by_id('signinUsername').send_keys(tdposUserCredentials.tdposUsername)
        driver.find_element_by_id('signinPassword').send_keys(tdposUserCredentials.tdposPassword)
        driver.find_element_by_name('signIn').click()
        driver.get('https://cloud.3dprinteros.com/printing/')   

        #tazTable = driver.find_element(By.XPATH, "//*[@id='id_box_51246']/span/table")
        #ultiTable = driver.find_element(By.XPATH, "//*[@id='id_box_51247']/span/table")
        #print("Taz 6 Queue" +tazTable.text +"/n Ultimaker Table /n" +ultiTable.text)
        return driver
        
    #stub method to close the passed open driver, may be irrelevant because of global.driver.close()
    def closeDriver(self):
        webdriver.Chrome().close()
        
    
    def search(self, driver, username):
        print('search method called')
        #create x path search string 
        #xpathSearch = "//*[contains(.,'"+username+"')]"
        xpathSearch = "//*[text()[contains(.,'"+username+"')]]"
        #returns a list of elements with that name 
        #there is some issue here where the top Taz queue: "Lultzbot Taz 6 Queue Lulzbot TAZ6" is not searchable...sometimes. The "DO NOT AUTHORIZE- TEMPORARY USER Lulzbot TAZ6" is searchable
        
        webElementList = driver.find_elements_by_xpath(xpathSearch)
        for i in webElementList:
            print((i.find_element_by_xpath('..')).text)
        #print(webElementList)
        #Goes two up from that element to get all the job data associated
        x= len(webElementList)-2
        '''
        for i in range(len(webElementList)):
            print (webElementList[i].text)
        print(x)
        '''
        #finds if the ultimaker or taz is mentioned to determine the queue name
        queueName = (webElementList[len(webElementList)-4].text)
        #this if statement transforms the queue name into a form that the Google form will take as input
        if('Ultimaker' in queueName):
            #print ('Queue is ultimaker')
            queueName = 'Ultimaker 3'
        elif('TAZ6' or 'TAZ' in queueName):
            #print ('Queue is TAZ6')
            queueName = 'Lulzbot Taz 6'
        else:
            #print("queue name not found")
            queueName = 'NaN'
        #all the print info, unparsed, raw
        printDetails = webElementList[x].text
        print('the print details or web elements.text:', printDetails)

        #should call the parser as a helper method and just return the printjob data structure
        printJobDict = TdposMiner.parser(printDetails, queueName)
        #print('the printjob dict:')
        #print(printJobDict)
        return printJobDict

    @staticmethod
    #manual line in for testing  
    def parser(string, queueName):
        #creates an array called splitString
        splitString = string.split(" ")
        print("this is the split string list:")
        print(splitString)
        #finds gcode in the list, then makes it a marker to navigate the list from 
        #should really have a try block around this for statement
        for text in splitString:
            if 'gcode' in text:
                #print(text)
                #print (splitString.index(text))
                printNameIndex = splitString.index(text)
            elif '.stl' in text:
                printNameIndex = splitString.index(text)
            
        # Retrieve the Index of EST
        #should really have a try block around this for statement
        for text in splitString:
            if 'EST' in text:
                #print(text)
                #print (splitString.index(text))
                estIndex = splitString.index(text)
            
        #iterates from the EST string item to the .gcode, adding all to the print name
        #need to use .join here in the range, may need to make a new temp list in the range
        #this seems like a very complex way to join items in a range in a list
        tempList = []
        for i in range(estIndex+1, printNameIndex+1):
            tempList.append(splitString[i])
        print('tempList', tempList) 
        printName = ('_'.join(tempList))
        print('printname', printName)
           # printName = str(splitString[i])
            
        #print(printName)
        #define all variables to create the printjob object
        date = splitString[0]
        time = splitString[1]
        printName = printName
        email = splitString[printNameIndex+1]
        weight = splitString[printNameIndex+2]
        duration = splitString[printNameIndex+4]
        #job ID parsing to remove the integers from the string
        #jobId = splitString[printNameIndex+10]
        jobId = string
        jobId = re.findall(r'\d\d\d\d\d', jobId)
        jobId = str(jobId[0])

    
        #print(date, time, printName, email, weight, duration,queueName)
        #creates the identified print object
        #printName = printJob.printJob(date, time, printName, email, weight, duration, queueName)
        printName = {"date":date, 
                    "time":time,
                    "printName": printName, 
                    "email":email, 
                    "weight":weight, 
                    "duration":duration, 
                    "jobId":jobId,
                    "queueName":queueName}
        #print(printName)
        #CONSIDER having this return a json object string instead
        return printName

#15.12.2018 17:08 EST	Spiral sphere_ornament_2013-11-23.gcode	Ultimaker 3 - 05	gr-fisprototypinglab@wpi.edu	U3, PLA, 0.25		4.13g	40m / 46m
#what the actual return text looks like:
#25.12.2018 21:09 EST Viking Duck.gcode emerrill@wpi.edu 6.09g $0.00 00:36 / - In queue Job ID:663678, Printer ID:51246
'''
TODO
-figure out how to parse file names with spaces
        -regex for find date: /^(?:[^ ]*\ ){2}([^ ]*)/g
-develop seperate search methods for part names and usernames
-whenever the program fails the thing doesn't close...need better error hadling, or any at all
-create a printjob object out of the collected
-be able to ask again if first email is bad
-re-architect so it can be run without opening, closing webbrowser
-solve the multiple files by one user problem
-figure out how to dump into a google sheet
-write a response script to fill out the google form as well
-sort out existing methods and classes

long term goals
write a class check helper which will be integrated into the class search function and refrences a text document with the list of names 
configure on pi
connect to printer
'''