# WPI3dPrinterOS_Interface

This is an attempt to streamline the queuing system of the WPI 3d print lab. 

#Current Operation

To use run the 'commandLineInterface' file. 

*what this does

-a test chrome browser is opened 

-the program logs into 3dprinteros with WPI's credentials *yes, I know this is very insecure*

-the test browser navigates the queuepage

-once on the queuepage, the program prompts the user for input in the command line

-this command line input and the webdriver is passed to the 3dpos search function (Tdpos.search)

  -selenium searches for the username, then goes up two web element levels to obtain all of the job information in a string form (printDetails)
  
  -then it goes up four levels from the username to find the queue name
  
  -now the parser is called and the printDetails list and queuename are passed
  
    -the parser takes printDetails string and slices and dices it into a dict which has all the formatting needed to be put in a form
    
    -the dict is returned
    
-after receiving the dict, it is printed and the user confirms this is the print they want

-Once selecting yes, the user inputs color and name, *class, material, and basic/full user coming soon*

-the information is added the the printDetails dict, and then put in a prefilled google forms url and posted to the sheet.

##todo:

-Clean the heaping pile of trash that is this program. There are a bunch of unused imports and unused files, but some may be useful for building an interface in the future(with flask or tinter, they're both here!)

-enable class input

-a way to select multiple prints, right now the first thing found in the list that matches the email is used
