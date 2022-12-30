#!/bin/bash

# Create a bash script that launches a menu system with the following options:
# Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)

PS3='Please enter your choice: '
options=("Option 1" "Option 2" "Option 3" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Option 1")
            echo "Hello World!"
            ;;
        "Option 2")
            echo "Ping 127.0.0.1"
            ping '127.0.0.1'
            ;;
        "Option 3")
            echo "IP info"
            ip a
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

# End


