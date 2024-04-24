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

#Write a Python program to get the smallest number from a list.
def smallest_num_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min

print(smallest_num_in_list([3, 5, -5, 10]))
