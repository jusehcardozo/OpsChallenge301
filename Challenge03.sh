#!/bin/bash

# Script: Ops 301 Challenge 03
# Author: Jose Cardozo
# Date of latest version:  12/14/22
# Purpose: File Permissions in Linux

# Prompts user for input directory path.
# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
# Navigates to the directory input by the user and changes all files inside it to the input setting.
# Prints to the screen the directory contents and the new permissions settings of everything in the directory.

# This command shows the User and Group that owns the file

ls -al

echo "Enter a directory path"
read directorypath

echo "Create a directory"
mkdir $thepath

# Create a file for testing
touch filetest.txt

# Asking permission for the directory
echo "Permition number for directory (i.e 777, 755)"
read pernumber

chmod --recursive $pernumber .

# List permission for directory
ls -al .

# End
