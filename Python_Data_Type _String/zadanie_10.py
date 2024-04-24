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

#Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
# zdefiniowanie funkcji, przejmujacej 'str1' (ciąg znaków).
def change_string(str1):
    # zwrocenie 'str1', przestawiając jego ostatni znak na pierwszą pozycję
    return str1[-1:] + str1[1:-1] + str1[:1]

# Wywołanie funkcji
print(change_string('kubatrzaskowski'))
print(change_string('123123'))
