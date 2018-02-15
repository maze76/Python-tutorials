# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 23:18:45 2018

@author: Zeljko
"""


"""
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer 
between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess 
too high or too low? Using bisection search, the computer will 
guess the user's secret number!

"""


print("Please think of a number between 0 and 100: ")
numGuesses = 0
low = 0
high = 100
guess = int((high + low) / 2)

while True:
    print("Is your secret number", guess, "?") 
    clar = input("Enter 'h' to indicate the guess is too high. " +
          "Enter 'l' to indicate the guess is too low. " +
          "Enter 'c' to indicate I guessed correctly.")
    if clar == "h":
        high = guess
    elif clar == "l":
        low = guess
    elif clar == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
    guess = int((high + low) / 2)
    numGuesses +=1
    
print("Game over. Your secret number was: ", int(guess))