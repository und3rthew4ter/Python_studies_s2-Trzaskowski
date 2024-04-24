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

#Write a Python script to sort (ascending and descending) a dictionary by value.
# biblioteka operator umozliwia sortowanie
import operator

d = {1: 2, 3: 5, 7: 3, 2: 1, 10: 0}

print('Original dictionary : ',d)

sorted_d = sorted(d.items(), key=operator.itemgetter(1))

print('Dictionary in ascending order by value : ',sorted_d)

sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1), reverse=True))

print('Dictionary in descending order by value : ',sorted_d)
