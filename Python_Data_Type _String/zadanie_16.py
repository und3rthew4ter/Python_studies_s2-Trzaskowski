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

#Write a Python function to insert a string in the middle of a string.
#Sample function and result :
#insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
#insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
# Zdefiniuj funkcję o nazwie insert_string_middle, która przyjmuje dwa argumenty: 'str' (ciąg znaków) i 'word' (słowo do wstawienia).
def insert_string_middle(str, word):
    # Utwórz i zwróć nowy ciąg znaków poprzez konkatenację pierwszych dwóch znaków 'str',
    # a następnie 'word', i na końcu pozostałych znaków 'str' od trzeciego znaku.
    return str[:2] + word + str[2:]

# Wywołaj funkcję insert_string_middle z różnymi ciągami wejściowymi i słowami, a następnie wydrukuj wyniki.
print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))
print(insert_string_middle('<<>>', 'HTML'))
