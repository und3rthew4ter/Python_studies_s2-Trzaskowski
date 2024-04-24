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

#zadanie 17
""" Write a Python program to print the alphabet pattern 'A'.
Expected Output:

  ***
 *   *
 *   *
 *****
 *   *
 *   *
 *   *

"""
result_str = ""
for row in range(0, 7):
    for column in range(0, 7):

        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "

    result_str = result_str + "\n"

print(result_str)