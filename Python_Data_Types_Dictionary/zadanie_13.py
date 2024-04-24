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

#Write a Python program to map two lists into a dictionary.
keys = ['czerwony', 'zielony', 'niebieski']

values = ['#FF0000', '#008000', '#0000FF']

color_dictionary = dict(zip(keys, values))

print(color_dictionary)
