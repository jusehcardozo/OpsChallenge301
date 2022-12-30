#!/usr/bin/env python3

# Script: Ops 301 Challenge 12
# Author: Jose Cardozo
# Date of latest version:  12/28/2022
# Purpose: Python Requests Library

# THIS WAS DONE BY USING THE DIRECTIONS OF THE RECORDING ETHAN DID, THIS IS NOT MY CREATION!!!

# First you'll need to install the requests library to your system
# Next, like any library, import it into your Python script
import requests

# Assign a requests.get function to a variable. Be sure to pass a parameter (the URL) into the function for it to work.
# response = requests.get('https://api.github.com')
aim = 'https://api.github.com'
# [404] = 'Site not found'
# HTTP Method Options:
print("Choose between options:")
print("1. GET\n2. POST\n3. PUT\n4. DELETE\n5. HEAD\n6. PATCH\n7. OPTIONS")

method_choice = input()
method_choice = int(method_choice)
print(type(method_choice))

if method_choice == 1:
    print(requests.get(aim))

if method_choice == 2:
    print(requests.post(aim))

if method_choice == 3:
    print(requests.put(aim))

if method_choice == 4:
    print(requests.delete(aim))

if method_choice == 5:
    print(requests.head(aim))

if method_choice == 6:
    print("Site not found")

elif method_choice == 7:
    print(requests.options(aim))  

# Print the status code obtained by the function using [var name].status code
# print(response.status_code)
else:
    print("wrong choice bro")
