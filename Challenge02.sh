#!/bin/bash

# Script: Ops 301 Challenge 09
# Author: Jose Cardozo
# Date of latest version:  12/30/2022
# Purpose: Date and Time


# How to show time and date
day=$(date +%D%T)

Copies /var/log/syslog to the current working directory
cp /var/log/syslog .

# Appends the current date and time to the filename
mv syslog syslog_$day

# End
