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

#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
# Definiowanie fukncji change_char, przyjmującej 'str1'.
def change_char(str1):
    # pobranie i przechowanie pierwszego znaku.
    char = str1[0]

    # zamiana wystąpień znaku 'char' na '$' w ciągu 'str1'.
    str1 = str1.replace(char, '$')

    # rekonstrukcja ciągu 'str1', umieszczając oryginalny znak 'char' jako pierwszy znak,
    # a następnie zmodyfikowany ciąg rozpoczynający się od drugiego znaku.
    str1 = char + str1[1:]

    # zwrocenie
    return str1

#wywylanie funkcji i wypisanie wyniku
print(change_char('restart'))  # Wynik: 'resta$t'
