
#How to modify the pre-filled Google SHeets URL to submit on post
#https://www.reddit.com/r/learnprogramming/comments/32xd4s/how_can_i_use_python_to_submit_a_google_form_or/
import requests
#the new google form URL:
#https://docs.google.com/forms/d/e/1FAIpQLSeGLNIhUCkON1tQJpbe9wIzrgUPIsfYB5QrNYDyNOAoeY-xVQ/viewform?usp=pp_url&entry.1102589694=StudentName&entry.799051989=Email&entry.1829673705=PrintName&entry.1926296081=Lulzbot+Taz+6&entry.1723229820=1hr+2min&entry.1191086835=JobID&entry.1878466307=ColorPreference&entry.546565404=PLA&entry.1416598942=__other_option__&entry.1416598942.other_option_response=Class&entry.533100273=Basic
payload = {'entry.1349225380':'print+nameTEST'}
class googleSheetsPoster:
    #the main method for the whole class. It takes all the form data as args, then posts it. 
    #I think it may be best to have the printjob and any other misc data required be submitted instead of having every form field as an arg. 
    @staticmethod
    #arguments it could take:
    #printName, username, printer, weight, time, employee, userType, material, color, Class, notes
    def fillForm(printJobDict):
        #new form ID:
        #https://docs.google.com/forms/d/e/1FAIpQLSeGLNIhUCkON1tQJpbe9wIzrgUPIsfYB5QrNYDyNOAoeY-xVQ/viewform?usp=pp_url&entry.1102589694=NAME&entry.799051989=EMAIL&entry.1829673705=PRINTNAME&entry.1926296081=Lulzbot+Taz+6&entry.1723229820=0h+0m&entry.1191086835=12345&entry.1878466307=COLOR&entry.546565404=PLA&entry.533100273=Basic
        formId = '1FAIpQLSeGLNIhUCkON1tQJpbe9wIzrgUPIsfYB5QrNYDyNOAoeY-xVQ'
        url = 'https://docs.google.com/forms/d/e/'+formId+'/formResponse?usp=pp_url'+'&entry.1102589694='+str(printJobDict.get('customerName'))+'&entry.799051989='+str(printJobDict.get('email'))+'&entry.1829673705='+str(printJobDict.get('printName'))+'&entry.1926296081='+str(printJobDict.get('queueName'))+'&entry.1723229820='+str(printJobDict.get('duration'))+'&entry.1191086835='+str(printJobDict.get('jobId'))+'&entry.1878466307='+str(printJobDict.get('colorPref'))+'&entry.546565404='+'PLA'+'&entry.533100273='+'Basic'
        #This is where the data is actually posted
        response = requests.post(url)
        print(type(response))
        #print(url)
        
        if ('200' in response):
            print("sucessfully submitted to form")
            return
        else: 
            print('there was an error:', response)
            return