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

#Write a Python program to multiply all the items in a list.
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

#wywolanie funkcji
print(multiply_list([4, 22, -8]))
