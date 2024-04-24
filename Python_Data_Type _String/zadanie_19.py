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

#Write a Python program to get the last part of a string before a specified character.
#https://www.w3resource.com/python-exercises
#https://www.w3resource.com/python
str1 = 'https://www.w3resource.com/python-exercises/string'

# Użyj metody rsplit() z '/' jako separatorem, aby podzielić ciąg od prawej strony,
# a [0] oznacza część przed ostatnim znakiem '/'. Następnie wydrukuj wynik.
print(str1.rsplit('/', 1)[0])


print(str1.rsplit('-', 1)[0])
