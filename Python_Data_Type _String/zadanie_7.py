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

#Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'
# definiowanie funkcji przyjmujacej 'str1'.
def not_poor(str1):
    # Znajdź indeks podciągu 'not' w ciągu wejściowym 'str1' i przechowaj go w 'snot'.
    snot = str1.find('not')

    # Znajdź indeks podciągu 'poor' w ciągu wejściowym 'str1' i przechowaj go w 'spoor'.
    spoor = str1.find('poor')

    # Sprawdź, czy 'poor' występuje po 'not' i zarówno 'not', jak i 'poor' są obecne w ciągu.
    if spoor > snot and snot > 0 and spoor > 0:
        # Zastąp podciąg od 'snot' do 'spoor+4' (włącznie) podciągiem 'good'.
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        # Jeśli warunki nie są spełnione, zwróć oryginalny ciąg 'str1'.
        return str1

# wywolanie i wypisanie funkcji
print(not_poor('The lyrics is not that poor!'))  # Wynik: 'The lyrics is good!'
print(not_poor('The lyrics is poor!'))          # Wynik: 'The lyrics is poor!'
