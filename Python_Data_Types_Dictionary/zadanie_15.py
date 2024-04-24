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

#Write a Python program to get the maximum and minimum values of a dictionary.
my_dict = {'x': 400, 'y': 5474, 'z': 521}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))

key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('maxymalna wartosc: ', my_dict[key_max])

print('minimalna wartosc: ', my_dict[key_min])
