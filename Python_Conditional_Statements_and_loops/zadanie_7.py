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

#Write a Python program that prints each item and its corresponding type from the following list.
#Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

for item in datalist:
    print("Type of", item, "is", type(item))
