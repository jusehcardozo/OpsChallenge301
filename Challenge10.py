#!/usr/bin/env python3

# Script: Ops 301 Challenge 10
# Author: Jose Cardozo
# Date of latest version:  12/23/2022
# Purpose: Python File Handling

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
