#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Win_JumP
#
# Created:     24.04.2024
# Copyright:   (c) Win_JumP 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#zadanie 19
"""Write a Python program to print the alphabet pattern 'E'.
Expected Output:

 *****
 *
 *
 ****
 *
 *
 *****

"""
def print_E():
    pattern = [
        "*****",
        "*",
        "*",
        "****",
        "*",
        "*",
        "*****"
    ]
    for line in pattern:
        print(line)

print_E()
