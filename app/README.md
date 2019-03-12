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

## Known Issues:

- need to submit the actual print time

- when no prints are found, need to throw an error

## todo:

- ability select multiple prints

- make more error handling, specific areas include: printjob list selection.

- enable class input for MQP, ES1310 etc
  - make a way to crosscheck WPI ID with class rosters

- create a UI
    -thinking a one page website with vue.js and a flask website

- consider an SQL database or Pandas Dataframe for better management of multiple prints and more flexible search terms

- make it run on raspberry PI

- connect a Thermal Printer

- re-write the whole thing in js 