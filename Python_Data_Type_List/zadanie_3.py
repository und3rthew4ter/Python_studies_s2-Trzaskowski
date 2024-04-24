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

#Write a Python program to get the largest number from a list.
def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max

print(max_num_in_list([1, 2, -8, 0]))
