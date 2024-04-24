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

#Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red
# Poproś użytkownika o wprowadzenie ciągu słów oddzielonych przecinkami i zapisz go w zmiennej 'items'.
items = input("napisz cos korzystajac z przecinkow ")

words = [word.strip() for word in items.split(",")]

unique_words = list(set(words))2

sorted_words = sorted(unique_words)
result = ",".join(sorted_words)
print(result)
