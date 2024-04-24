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

#Write a Python program that accepts a word from the user and reverses it.
word = input("wprowadz slowo do odrocenia jego kolejnosci: ")

for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")

print("\n")
