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

#Write a Python program to count the number of even and odd numbers in a series of numbers
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#Expected Output :
#Number of even numbers : 5
#Number of odd numbers : 4

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

count_odd = 0
count_even = 0

for x in numbers:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1

print("liczba parzysta:", count_even)
print("liczba nieparzysta:", count_odd)
