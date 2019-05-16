#This is a program which checks the full user list on startup and loads it into a dict. Ideally, this will be put in a drive folder in the future
import globals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tdposUserCredentials

class check_users():

        def obtain_users(self):
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--log-level=3")

                globals.permissionsDriver = webdriver.Chrome(chrome_options=chrome_options)
                globals.permissionsDriver.get('https://cloud.3dprinteros.com/printing/')
                globals.permissionsDriver.find_element_by_id('signinUsername').send_keys(tdposUserCredentials.tdposUsername)
                globals.permissionsDriver.find_element_by_id('signinPassword').send_keys(tdposUserCredentials.tdposPassword)
                globals.permissionsDriver.find_element_by_name('signIn').click()
                globals.permissionsDriver.get('https://cloud.3dprinteros.com/users/') 
                #need to find the name, display them all, and then scrape them and the user permissions into an array of some kind
                globals.userList
                return userList


        def check_user_permission(self, user):
                if user in globals.userList.permissions:

                        return user.permission
                else:
                        raise Exception("user does not have permission to use the print lab. Check the users list.***need a url link to that here***")
                                