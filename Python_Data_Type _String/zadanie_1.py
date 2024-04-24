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

#1. Write a Python program to calculate the length of a string.
# Zdefiniuj funkcję o nazwie string_length, która przyjmuje jeden argument, str1.
def string_length(str1):
    # Zainicjuj zmienną count na 0, aby śledzić długość ciągu znaków.
    count = 0

    # Iteruj przez każdy znak w ciągu wejściowym str1.
    for char in str1:
        # Dla każdego napotkanego znaku zwiększ count o 1.
        count += 1

    # Zwróć ostateczny count, który reprezentuje długość ciągu wejściowego.
    return count

# Wywołaj funkcję string_length z argumentem 'w3resource.com' i wydrukuj wynik.
print(string_length('TrzaskowskiJakub'))
