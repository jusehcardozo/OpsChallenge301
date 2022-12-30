#!/usr/bin/env python3

# Script: Ops 301 Challenge 11
# Author: Jose Cardozo
# Date of latest version:  12/27/2022
# Purpose: Psutil

# Create a Python script that fetches this information using Psutil:
import psutil

output = psutil.cpu_times()
print(output)

# Time spent by normal processes executing in user mode
print("Time spent in user mode:")
print(output.user)

# Time spent by processes executing in kernel mode
print("Time spent by processes executing in kernel mode:")
print(output.system)

# Time when system was idle
print("Time when system was idle:")
print(output.idle)

# Time spent by priority processes executing in user mode
print("Time spent by priority processes executing in user mode:")
print(output.nice)

# Time spent waiting for I/O to complete.
print("Time spent waiting for I/O to complete:")
print(output.iowait)

# Time spent for servicing hardware interrupts
print("Time spent for servicing hardware interrupts:")
print(output.irq)

# Time spent for servicing software interrupts
print("Time spent for servicing software interrupts:")
print(output.softirq)

# Time spent by other operating systems running in a virtualized environment
print("Time spent by other operating systems running in a virtualized environment:")
print(output.steal)

# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print("Time spent running a virtual CPU for guest operating systems under the control of the Kernel:")
print(output.guest)
