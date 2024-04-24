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

# Write a Python program to remove duplicates from a list.
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

dup_items = set()
uniq_items = []

for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
