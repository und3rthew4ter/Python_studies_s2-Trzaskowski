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

#Write a Python function to reverse a string if its length is a multiple of 4.
def reverse_string(str1):
    if len(str1) % 4 == 0:
        return ''.join(reversed(str1))

    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))
