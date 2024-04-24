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

#Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# Zdefiniuj funkcję o nazwie char_frequency, która przyjmuje jeden argument, str1.
def char_frequency(str1):
    # Zainicjuj pusty słownik o nazwie 'dict' do przechowywania częstości występowania znaków.
    dict = {}

    # Iteruj przez każdy znak 'n' w ciągu wejściowym str1.
    for n in str1:
        # Pobierz klucze (unikalne znaki) w słowniku 'dict'.
        keys = dict.keys()

        # Sprawdź, czy znak 'n' jest już kluczem w słowniku.
        if n in keys:
            # Jeśli 'n' jest już kluczem, zwiększ jego wartość (częstość) o 1.
            dict[n] += 1
        else:
            # Jeśli 'n' nie jest kluczem, dodaj go do słownika z częstością 1.
            dict[n] = 1

    # Zwróć słownik zawierający częstość występowania każdego znaku w ciągu wejściowym.
    return dict

# Wywołaj funkcję char_frequency z argumentem 'google.com' i wydrukuj wynik.
print(char_frequency('google.com'))
