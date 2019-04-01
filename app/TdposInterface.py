from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import printJob
import re
import commandLineInterface
import tdposUserCredentials
import globals

class TdposMiner() :
    
    def initializeListener(self):
        driver = webdriver.Chrome()
        #login procedure. Will need to make username and password gui inputs in future
        driver.get('https://cloud.3dprinteros.com/printing/')
        driver.find_element_by_id('signinUsername').send_keys(tdposUserCredentials.tdposUsername)
        driver.find_element_by_id('signinPassword').send_keys(tdposUserCredentials.tdposPassword)
        driver.find_element_by_name('signIn').click()
        driver.get('https://cloud.3dprinteros.com/printing/')   
        #these might be useful for inserting into an sql table later
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
        webElementList = driver.find_elements_by_xpath(xpathSearch)
        jobMatchList = []
        for i in webElementList:
            #This searches the inner HTML via Xpath
            #jobMatchList.append(i.find_element_by_xpath('..').text+i.find_element_by_xpath('../td[4]').get_attribute('innerHTML'))
            printEntry = (i.find_element_by_xpath('..').text)
            #goes up three levels to find all the text in that queue, this includes the queuename!
            queueText = ((i.find_element_by_xpath('../../..')).text)
            if 'Ultimaker 3' in queueText:
                printEntry = printEntry + (' Ultimaker 3')
            elif 'Taz' in queueText:
                printEntry = printEntry + (' Lulzbot Taz 6')
            else: 
                #this should be an error 
                printEntry = printEntry + (' QUEUENAME NOT FOUND')

            jobMatchList.append(printEntry)
        #iterate through the list to remove the already queued prints
        for i in jobMatchList: 
            if "In queue" not in i:    
                del i
        return jobMatchList
        
    def parser(self, string):
        #creates an array called splitString
        splitString = string.split(" ")
        print(splitString)
        #finds gcode in the list, then makes it a marker to navigate the list from 
        #should really have a try block around this for statement
        try:
            for text in splitString:
                if 'wpi' in text:
                    #finds the index of the UserName
                    userNameIndex = (splitString.index(text))
                    pass
        except Exception as e2:
            raise Exception('Cannot queue prints for non WPI emails. This is email is: ', text)
            print(e2)
        
        #new statement to find the printname index based on the grams
        #tempGrams = re.findall(r'/\d\d/g',splitString)
        #print ('tempgrams: ', tempGrams)

        # Retrieve the Index of EST
        #should really have a try block around this for statement
        #est/edt is for daylight savings
        for text in splitString:
            match = re.search(r'\d\d\:\d\d', text)
            if match:
                #print('found match', match.group())
                timeIndex = splitString.index(match.group())
                #print('timeIndex: ', timeIndex)
                #leave the for loop as soon as the first match is found
                break
            
        #iterates from the EST string item to the .gcode, adding all to the print name
        #need to use .join here in the range, may need to make a new temp list in the range
        #this seems like a very complex way to join items in a range in a list
        tempList = []
        #print('time index, username index:', timeIndex ," , " , userNameIndex)
        for i in range(timeIndex+1, userNameIndex):
            tempList.append(splitString[i])
        #the %20 is an expiremental way to add spaces to print names
        printName = ('%20'.join(tempList))
        #print("printName: ", printName)

    
        #define all variables to create the printjob object
        date = splitString[0]
        time = splitString[1]
        printName = printName
        email = splitString[userNameIndex]
        weight = splitString[userNameIndex+1]
        duration = splitString[userNameIndex+3]
        #print(duration)
        #at this point this is a string with the format hh:mm
        splitDuration = duration.split(':')
        duration = (splitDuration[0]+'h%20'+ splitDuration[1]+'m')
        #print(duration)
        #job ID parsing to remove the integers from the string
        #jobId = splitString[userNameIndex+10]
        jobId = string
        jobId = re.findall(r'\d\d\d\d\d\d', jobId)
        jobId = str(jobId[0])
        #now find the queuename with a similar method
        queueName = string
        #there are a bunch of numbers with four digits, so a list is returned
        if 'Ultimaker' in splitString:
            queueName = 'Ultimaker%203'
        elif 'Taz' in splitString:
            queueName = 'Lulzbot%20Taz%206'

        #print(date, time, printName, email, weight, duration, queueName)
        #creates the identified print Dictionary object
        printInfo = {"date":date, 
                    "time":time,
                    "printName": printName, 
                    "email":email, 
                    "weight":weight, 
                    "duration":duration, 
                    "jobId":jobId,
                    "queueName":queueName}
        '''
        #for debugging purposes, see where the data is put in the dict, and if anything is missing
        print('date: ', printInfo["date"])
        print('time: ', printInfo["time"])
        print('printName: ', printInfo["printName"])
        print('email: ', printInfo["email"])
        print('weight: ', printInfo["weight"])
        print('duration: ', printInfo["duration"])
        print('jobID: ', printInfo["jobId"])
        print('queueName: ', printInfo["queueName"])
        '''
        #print(printName)
        return printInfo
'''
    @staticmethod
    def printDict(dictionary):
        for key, value in dictionary:
            print(i.index(), i)
'''

#15.12.2018 17:08 EST	Spiral sphere_ornament_2013-11-23.gcode	Ultimaker 3 - 05	gr-fisprototypinglab@wpi.edu	U3, PLA, 0.25		4.13g	40m / 46m
#what the actual return text looks like:
#25.12.2018 21:09 EST Viking Duck.gcode emerrill@wpi.edu 6.09g $0.00 00:36 / - In queue Job ID:663678, Printer ID:51246
'''
TODO

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