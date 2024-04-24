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

#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'
# definiowanie funkcji, przyjmujacej 'str1'.
def add_string(str1):
    # Pobierz długość ciągu wejściowego 'str1' i przechowaj ją w zmiennej 'length'.
    length = len(str1)

    # Sprawdź, czy długość 'str1' jest większa niż 2 znaki.
    if length > 2:
        # Jeśli ostatnie trzy znaki 'str1' to 'ing', dodaj 'ly' na końcu.
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            # dodanie inga na koniec.
            str1 += 'ing'

    # zwrocenie
    return str1

# Wywolanie i wypisanie funkcji
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
