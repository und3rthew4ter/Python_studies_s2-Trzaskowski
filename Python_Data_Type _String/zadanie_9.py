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

# Write a Python program to remove the nth index character from a nonempty string.
# zdefiniowanie funkcji przyjmującej 'str' (ciąg znaków) i 'n' (indeks znaku do usunięcia).
def remove_char(str, n):
    # Utwórz nowy ciąg znaków 'first_part', który zawiera wszystkie znaki od początku 'str' do znaku o indeksie 'n' (nie włącznie).
    first_part = str[:n]

    # Utwórz nowy ciąg znaków 'last_part', który zawiera wszystkie znaki od znaku o indeksie 'n+1' do końca 'str'.
    last_part = str[n+1:]

    #zwrocenie
    return first_part + last_part

# wywolanie funkcji i jej wypisanie.
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))
