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

#Write a Python program to remove a key from a dictionary.
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(myDict)

if 'a' in myDict:
    del myDict['a']

print(myDict)
