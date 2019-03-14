
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
        print(url)
        #+'&entry.1416598942='+ no class option right now
        #how does this wokr? &entry.1416598942=ME+2300&
         # Set destination URL here
        
        #This is where the data is actually posted
        print(requests.post(url))
        '''
        if '<Response [200]>' in requests.post(url):
            print("sucessfully submitted to form")
        '''
'''
def main():
    googleSheetsPoster.fillForm()

if __name__ == '__main__':
    main()



#print(json)

#https://docs.google.com/forms/d/e/1FAIpQLSf369fAiB4-6x6cFQjopzRjnPamtzlaCV6DnGNE5dIil9_OEg/
#formResponse?usp=pp_url
# &entry.1349225380=PRINT+NAME
# &entry.837729285=EMERRILL
# &entry.1675741116=Lulzbot+TAZ6
# &entry.779264003=10&entry.740044429=10
# &entry.648955311=ETHAN&entry.237693438=Basic+User
# &entry.559059428=PLA
# &entry.86368064=COLOR
# &entry.752137210=ME2300&entry.2144647461=NOTES
'''