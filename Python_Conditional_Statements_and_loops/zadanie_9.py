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

#Write a Python program to get the Fibonacci series between 0 and 50.
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34

x, y = 0, 1

while y < 50:
    print(y)

    x, y = y, x + y
