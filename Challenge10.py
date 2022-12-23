#!/usr/bin/env python3

# Script: Ops 301 Challenge 09
# Author: Jose Cardozo
# Date of latest version:  12/22/2022
# Purpose: Using Conditionals

import os

# Using file handling commands, create a Python script that creates a new .txt file,

f = open("josefile.txt", "w")

# Appends three lines,

line1 = "Merry\n"
line2 = "Christmas\n"
line3 = "To You All"

f.write(line1)
f.write(line2)
f.write(line3)

# Prints to the screen the first line, 

f = open("josefile.txt", "r")

print(f.read())

# Then deletes the .txt file.

os.remove("josefile.txt")

# End
