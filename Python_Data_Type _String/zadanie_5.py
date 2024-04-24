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

#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
# definiowanie funkcji chars_mix_up, która przyjmuje dwa argumenty 'a' i 'b'.
def chars_mix_up(a, b):
    # Utwórz nowy ciąg 'new_a', biorąc pierwsze dwa znaki z 'b' i łącząc je
    # z pozostałymi znakami z 'a' zaczynając od trzeciego znaku.
    new_a = b[:2] + a[2:]

    # Utwórz nowy ciąg 'new_b', biorąc pierwsze dwa znaki z 'a' i łącząc je
    # z pozostałymi znakami z 'b' zaczynając od trzeciego znaku.
    new_b = a[:2] + b[2:]

    # Połącz 'new_a', spację i 'new_b', aby utworzyć pojedynczy ciąg.
    return new_a + ' ' + new_b

#wywolanie i wypisanie funkcji
print(chars_mix_up('abc', 'xyz'))  # Wynik: 'xyc abz'
