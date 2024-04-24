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

#Write a Python program to multiply all the items in a dictionary. ()
my_dict = {'data1': 210, 'data2': -77, 'data3': 777}

result = 1

for key in my_dict:
    result = result * my_dict[key]

print(result)

