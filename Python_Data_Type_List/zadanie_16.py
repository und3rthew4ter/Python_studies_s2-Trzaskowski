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

# Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
# Define a function named printValues
def printValues():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])

printValues()
