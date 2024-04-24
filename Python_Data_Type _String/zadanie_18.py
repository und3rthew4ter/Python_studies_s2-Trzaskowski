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

#Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
#Sample function and result :
def first_three(str):
    if len(str) > 3:
        return str[:3]
    else:
        return str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))

