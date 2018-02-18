# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 09:10:29 2018

@author: Zeljko
"""
#%%

"""
Write an iterative function iterPower(base, exp) that 
calculates the exponential by simply using successive 
multiplication. For example, iterPower(base, exp) should 
compute by multiplying base times itself exp times. 
Write such a function below. 
This function should take in two values - base can be a 
float or an integer; exp will be an integer 0. 
It should return one numerical value. 
Your code must be iterative - use of the ** operator is 
not allowed.

"""
 
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result        
    
#%%    
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    result = 1
    for i in range(1, exp +1):
        result *= base
    return result


#%%
    
"""
In Problem 1, we computed an exponential by iteratively executing 
successive multiplications. We can use the same idea, but in a 
recursive function.

Write a function recurPower(base, exp) which computes base exp
by recursively calling itself to solve a smaller version of 
the same problem, and then multiplying the result by base 
to solve the initial problem.

This function should take in two values - base can be a 
float or an integer; exp will be an integer >= 0.
. It should return one numerical value. Your code must be 
recursive - use of the ** operator or looping constructs 
is not allowed.
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    
    for(2, 4)
    
    base*base*base*base = 16
    base * (base** (exp-1 times) = 2 * 8 = 16
    base * base * (base** (exp -2 times) = 2 * 2 * 4 = 16
    base*base*base(base**(exp -3 times)) = 2*2*2*2= 16
    base*base*base*base(base**(exp-4times))=2*2*2*2*1* = 16
    
    if exp == 0:
        return 1
    else:
        return base * (base ** (exp - 1))
        exp -= 1
    solution above works but this is without function call in 
    recursive step
    
    '''
    
    if exp == 0:
        return 1
    else:
        return base * recurPower(base,(exp - 1))
        
        
print(recurPower(2, 5))


#%%

