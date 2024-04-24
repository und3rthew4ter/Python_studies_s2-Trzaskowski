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

#Write a Python program to remove duplicates from the dictionary.
student_data = {
    'id1': {
        'imie': ['Klaudia'],
        'klasa': ['V'],
        'przedmioty': ['matematyka, angielski, polski, geografia']
    },
    'id2': {
        'imie': ['Eleonora'],
        'klasa': ['VI'],
        'przedmioty': ['matematyka, angielski, polski']
    },
    'id3': {
        'imie': ['Teodora'],
        'klasa': ['X'],
        'przedmioty': ['polski, geografia']
    },
    'id4': {
        'imie': ['Czeresnia'],
        'klasa': ['V'],
        'przedmioty': ['dzwonek']
    }
}

result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
