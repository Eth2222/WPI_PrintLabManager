# WPI3dPrinterOS_Interface

This is an attempt to streamline the queuing system of the WPI 3d print lab. 

# Credentials Required
- create a file named 'tdposUserCredentials'

- define a 'tdposUsername' and tdposPassword' as strings

 - for a future google sheets implementation:
https://developers.google.com/sheets/api/quickstart/python

follow the guide and put the created file in the root directory


# Current Operation

To use run the 'commandLineInterface' file. 

*what this does

- a test chrome browser is opened 

- the program logs into 3dprinteros with WPI's credentials *yes, I know this is very insecure*

- the test browser navigates the queuepage

-once on the queuepage, the program prompts the user for input in the command line

- this command line input and the webdriver is passed to the 3dpos search function (Tdpos.search)

  - selenium searches for the username, then goes up two web element levels to obtain all of the job information in a string form (printDetails)
  
  - then it goes up four levels from the username to find the queue name
  
  - now the parser is called and the printDetails list and queuename are passed
  
    - the parser takes printDetails string and slices and dices it into a dict which has all the formatting needed to be put in a form
    
    - the dict is returned
    
- after receiving the dict, it is printed and the user confirms this is the print they want

- Once selecting yes, the user inputs color and name, *class, material, and basic/full user coming soon*

- the information is added the the printDetails dict, and then put in a prefilled google forms url and posted to the sheet.

##ChangeLog (3/31/19)

- updated to be compatible with the March update of 3dprinteros 

- added spaces to print names

- now lists full job id in submission

- added more error handling throughout 

## Known Issues:

- when no prints are found, need to throw an error

## todo:

- ability select multiple prints

- reference the full user list and enter the information in the form

- split the initialize listener method. THis will enable a method which will only launch a headless instance of chrome with special settings. Another function can be created for the navigation to the user permissions and print queue pages for each driver.

- Cloud database for users

- cloud database for all prints. This would greatly enhance the speed of the program

- enable class input for MQP, ES1310 etc
  - make a way to crosscheck WPI ID with class rosters

- create a UI
    -thinking a one page website with vue.js and a flask website

- consider an SQL database or Pandas Dataframe for better management of multiple prints and more flexible search terms

- make it run on raspberry PI

- connect a Thermal Printer

- re-write the whole thing in js 

##Change log (05/15/19)

- Added Multiple Print Entry! 

- Re-architected the methods for a more intuitive program structure command, more work needed here. 

- began construction of user permissions checker


##Change log (3/31/19)

- updated to be compatible with the March update of 3dprinteros 

- added spaces to print names

- now lists full job id in submission

- added more error handling throughout 
