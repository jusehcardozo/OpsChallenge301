#!/usr/bin/env python3

# Script: Ops 301 Challenge 06
# Author: Jose Cardozo
# Date of latest version:  12/29/2022
# Purpose: Bash in Python

# The Python module "os" must be utilized
# At least three variables must be declared in Python that contain results of bash operations
# The Python function print() must be used at least three times
# Include execution of the following bash commands inside your Python script:

# whoami
# ip a
# lshw -short

# The Python module "os" must be utilized to run Bash with Python.
import os

# This command will say who I am.
whoami_output = os.system("whoami")

# This command will display information about IP addresses.
ip_a_output = os.system("ip a")

# This command will display details about my hardware configuration.
lshw_output = os.system("lshw -short")

print(whoami_output)
print(ip_a_output)
print(lshw_output)

# End 
