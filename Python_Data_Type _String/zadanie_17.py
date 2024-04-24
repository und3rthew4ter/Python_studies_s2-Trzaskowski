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

#Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
#Sample function and result :
#insert_end('Python') -> onononon
#insert_end('Exercises') -> eseseses
def insert_end(str):
    # Wyodrębnij ostatnie dwa znaki z ciągu wejściowego 'str' i zapisz je w zmiennej 'sub_str'.
    sub_str = str[-2:]

    return sub_str * 4

# Wywołaj funkcję insert_end z różnymi ciągami wejściowymi i wydrukuj wyniki.
print(insert_end('Python'))
print(insert_end('Exercises'))
