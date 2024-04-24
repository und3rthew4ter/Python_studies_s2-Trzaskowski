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

#Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius

temp = input("wprowadz temperature, ktora chcesz przeliczyc? (np., 45F, 102C itp.) : ")

degree = int(temp[:-1])

i_convention = temp[-1]

if i_convention.upper() == "C":
    # zamiana z celsusza na fahrenheita
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
    # zamiana z fahrenheita na celsjusza
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "celsjusz"
else:
    print("niepoprawne.")
    quit()

print("temperatura w", o_convention, "wynosi", result, "stopni.")
