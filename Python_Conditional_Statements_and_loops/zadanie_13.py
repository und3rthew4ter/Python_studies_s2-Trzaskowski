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

#Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.
#Sample Data : 0100,0011,1010,1001,1100,1001
#Expected Output : 1010

items = []

num = [x for x in input().split(',')]

for p in num:
    x = int(p, 2)

    if not x % 5:
        items.append(p)

print(','.join(items))
