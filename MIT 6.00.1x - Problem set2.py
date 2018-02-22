# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:43:47 2018

@author: Zeljko
"""
"""
Write a program to calculate the credit card balance after one 
year if a person only pays the minimum monthly payment required 
by the credit card company each month.

The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and 
remaining balance. At the end of 12 months, print out the 
remaining balance. Be sure to print out no more than two 
decimal digits of accuracy - so print for example 
Remaining balance: 813.41
"""


balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    
    minPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minPayment 
    interest = (annualInterestRate/12) * unpaidBalance 
    balance = unpaidBalance + interest
   
    
print("Remaining balance:", round(balance, 2))




#%%

"""
Now write a program that calculates the minimum fixed monthly 
payment needed in order pay off a credit card balance within 
12 months. By a fixed monthly payment, we mean a single number 
which does not change each month, but instead is a constant 
amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly 
payment rate.

The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly 
payment that will pay off all debt in under 1 year, for example:
Lowest Payment: 180     
    
 Assume that the interest is compounded monthly according to 
 the balance at the end of the month (after the payment for 
 that month is made). The monthly payment must be a multiple of 
 $10 and is the same for all months. Notice that it is possible 
 for the balance to become negative using this payment scheme, 
 which is okay. A summary of the required math is found below:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - 
    (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + 
    (Monthly interest rate x Monthly unpaid balance)
"""

balance = 3329
annualInterestRate = 0.2

monthlyPaymentRate = 10
x = balance

while balance > 0: 
    for i in range (12):
        
        unpaidBalance = balance - monthlyPaymentRate 
        interest = (annualInterestRate/12) * unpaidBalance 
        balance = unpaidBalance + interest
    if balance <= 0:
        break
    elif balance > 0:
        monthlyPaymentRate += 10
        balance = x        
    
    
print("Lowest Payment:", monthlyPaymentRate)
    
  
    
#%%    
#bisection search problem as above

epsilon = 0.01
low = balance / 12
high = ((balance * (1 + monthlyInterestRate)**12) / 12.0)    
ans = (high + low)/2.0

while ans >= epsilon:
    















#%%

x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print("low = " + str(low) + " high = " + str(high) + " ans " + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print("numGuesses = " + str(numGuesses))
print(str(ans) + " is close to square root of " + str(x))







    
    
    
    
    
    
    
    
    
    
    
    
    
    