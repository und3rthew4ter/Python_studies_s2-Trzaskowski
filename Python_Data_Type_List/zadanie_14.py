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

#Write a Python program to print the numbers of a specified list after removing even numbers from it.
num = [5, 3, 12, 21, 34, 50, 64]

num = [x for x in num if x % 2 != 0]
print(num)
