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

#Write a Python program to iterate over dictionaries using for loops.
d = {'zcerwony': 1, 'zielony': 2, 'niebieski': 3}

for color_key, value in d.items():
    print(color_key, 'powiązany z ', d[color_key])
