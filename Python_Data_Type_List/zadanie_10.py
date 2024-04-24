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

# Write a Python program to find the list of words that are longer than n from a given list of words.
def long_words(n, str):
    word_len = []

    txt = str.split(" ")

    for x in txt:
        if len(x) > n:
            word_len.append(x)

    return word_len

print(long_words(3, "Trzaskowski Jakub test apki eoe eo"))
