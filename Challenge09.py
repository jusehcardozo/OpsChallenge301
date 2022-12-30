#!/usr/bin/env python3

# Script: Ops 301 Challenge 09
# Author: Jose Cardozo
# Date of latest version:  12/22/2022
# Purpose: Using Conditionals

# Equals: a == b
a = 10
b = 10

if a == b:
    print("A is equal to B")

# Not Equals: a != b

a = 10
b = 20

if a != b:
    print("A is not equal B")

# Less than: a < b

a = 10
b = 20

if a < b:
    print("A is less than B")

# Less than or equal to: a <= b

a = 10
b = 20

if a <= b:
    print("A is less or equal to B")

# Greater than: a > b

a = 20
b = 10

if a > b:
    print("A is greater than B")

# Greater than or equal to: a >= b

a = 20
b = 10

if a >= b:
    print("A is greater or equal to B")

# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

a = 10
b = 20

if a == b:
    print("This is it, same value!")
elif a < b:
        print("This is the truth!")

# Create an if statement that includes both elif and else to execute when both if and elif are not met.

a = 10
b = 20

if a == b:
    print("This is right!")
elif a > b:
    print("Believe me, this is the actual truth!")
else: a <= b
print("Jackpot!")

# End
