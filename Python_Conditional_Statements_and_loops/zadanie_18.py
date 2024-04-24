#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Win_JumP
#
# Created:     24.04.2024
# Copyright:   (c) Win_JumP 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#zadanie 18
""" Write a Python program to print the alphabet pattern 'D'.
Expected Output:

 ****
 *   *
 *   *
 *   *
 *   *
 *   *
 ****

"""
def print_D():
    pattern = [
        "**** ",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        "**** "
    ]
    for line in pattern:
        print(line)

# Wywołanie funkcji do wyświetlenia wzorca litery 'D'
print_D()
