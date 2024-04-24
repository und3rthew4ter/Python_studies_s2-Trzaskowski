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

# Write a Python function that takes two lists and returns True if they have at least one common member.
# Define a function called 'common_data' that takes two lists, 'list1' and 'list2', as input
def common_data(list1, list2):
    result = False

    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))
