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

#Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2
def match_words(words):
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))
