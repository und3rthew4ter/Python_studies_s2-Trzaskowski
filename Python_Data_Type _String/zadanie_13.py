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

# Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# Poproś użytkownika o podanie ulubionego języka i zapisz odpowiedź w zmiennej 'user_input'.
user_input = input("twoj najulubienszy jezyk to? ")

# Wydrukuj wiadomość "My favorite language is" po czym dodaj odpowiedź użytkownika z konwersją na wielkie litery (uppercase).
print("moj najulubienszy jezyk to " + user_input.upper())

# Wydrukuj wiadomość "My favorite language is" po czym dodaj odpowiedź użytkownika z konwersją na małe litery (lowercase).
print("moj najulubienszy jezyk to  " + user_input.lower())
