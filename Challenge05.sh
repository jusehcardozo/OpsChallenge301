#!/bin/bash/

# Print to the screen the file size of the log files before compression
# Compress the contents of the log files listed below to a backup directory
# /var/log/syslog
# /var/log/wtmp
# The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
# Example: /var/log/backups/syslog-20220928081457.zip
# Clear the contents of the log file
# Print to screen the file size of the compressed file
# Compare the size of the compressed files to the size of the original log files


target1=syslog
 target2=wtmp

 backup_folder=~/backups


clear_log () {
    target_size$(stat -c%s /var/log/$1)

# print size before compression
    echo "the size of $s1 is $target_size"

 #  compress the contents of the log files to a backup directory
    back_name=$1.$(date +%F%H%M%S).zip
    zip $backup_folder/$back_name /var/log/$1
    target_size_compressed=$(stat -c%s $backup_folder/$backup_name)

# clear the log file
# cat /dev/null > /var/log/$1
# target_size_afterclearing+$ (stat  ~c%s /var/log/$1)
    echo "Size of original log: $target_size"
    echo "Size of compressed log: $target_size_compressed"
# echo "Size of cleared"
}

clear_log $target1
clear_log $target2301
