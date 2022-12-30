#!/usr/bin/env python3

# Import libraries

# Script must use the os.walk() function from the library.
import os


# Script must ask the user for a file path and user input string into a variable.
dir = input("Enter a directory name:")

# Script must use the os.walk() function within a python function that hands in the user input file path.
def directoryprint(dir):
    for (root, dirs, files) in os.walk(dir):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

directoryprint(dir)

# End
