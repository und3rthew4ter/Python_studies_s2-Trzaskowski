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

#Write a Python program to sort a given dictionary by key
color_dict = {
    'czerwony': '#FF0000',
    'zielony': '#008000',
    'czarny': '#000000',
    'biały': '#FFFFFF'
}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
