#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Win_JumP
#
# Created:     13.04.2024
# Copyright:   (c) Win_JumP 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
# Create an empty list named 'lines'
lines = []

while True:
    l = input()

    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)
