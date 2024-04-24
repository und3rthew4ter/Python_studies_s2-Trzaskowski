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

#Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
#Sample Data:
#([0, 3, 4, 7, 9]) -> False
#([3, 5, 7, 13]) -> True
#`([1, 5, 3]) -> False
def test(nums):
    return all(is_prime(i) for i in nums)

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

nums = [0, 3, 4, 7, 9]
print("Original list of numbers:")
print(nums)
print("Check if each number is prime in the said list of numbers:")
print(test(nums))

nums = [3, 5, 7, 13]
print("\nOriginal list of numbers:")
print(nums)
print("Check if each number is prime in the said list of numbers:")
print(test(nums))

nums = [1, 5, 3]
print("\nOriginal list of numbers:")
print(nums)
print("Check if each number is prime in the said list of numbers:")
print(test(nums))
