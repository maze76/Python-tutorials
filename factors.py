# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 21:22:23 2018

@author: Zeljko
"""


"""Real python I assignment: Find the factors of a number.
function to find all of the integers that devide evenly into an integer 
provided by user. Use % operator to check divisibility."""

number_1 = input("Enter a positive integer: ")
for i in range(1, (int(number_1) + 1)):
    if int(number_1) % i == 0:
        print(i, "is a divisor of", number_1)
     

    