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

#Write a Python program to remove characters that have odd index values in a given string.
# funkcja przyjmująca 'str' ciąg znakow
def odd_values_string(str):
    result = ""

    # Iteruj przez indeksy (i) znaków w ciągu wejściowym 'str'.
    for i in range(len(str)):
        # Sprawdź, czy indeks (i) jest parzysty (czyli ma resztę 0 przy dzieleniu przez 2).
        if i % 2 == 0:
            # Jeśli indeks jest parzysty, dodaj znak na tym indeksie do ciągu 'result'.
            result = result + str[i]

    return result

print(odd_values_string('trzaskowski'))
print(odd_values_string('trzaskowskijakubtest'))
