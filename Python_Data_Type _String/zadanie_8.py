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

#Write a Python function that takes a list of words and return the longest word and the length of the longest one.
#Sample Output:
#Longest word: Exercises
#Length of the longest word: 9
# zdefiniowanie funkcji
def find_longest_word(words_list):
    # Utwórz pustą listę 'word_len' do przechowywania par (długość słowa, słowo).
    word_len = []

    # Iteruj przez każde słowo 'n' w liście 'words_list'.
    for n in words_list:
        # Dodaj krotkę zawierającą długość słowa i samo słowo do listy 'word_len'.
        word_len.append((len(n), n))

    # Posortuj listę 'word_len' na podstawie długości słów (rosnąco).
    word_len.sort()

    # zwrocenie
    return word_len[-1][0], word_len[-1][1]

# wywolanie funkcji i zapisanie wyniku
result = find_longest_word(["PHP", "Exercises", "Backend"])

# wypisanie slowa i jego dlugosci
print("\nNajdłuższe słowo: ", result[1])
print("Długość najdłuższego słowa: ", result[0])
