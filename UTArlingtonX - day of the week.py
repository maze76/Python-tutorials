# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:30:06 2018

@author: Zeljko
"""

"""
Write a function that accepts a string which contains a particular date 
from the Gregorian calendar. Your function should return what day of the 
week it was. Here are a few examples of what the input string(Month Day Year) 
will look like. However, you should not 'hardcode' your program to work only 
for these input!

"June 12 2012"
"September 3 1955"
"August 4 1843" 

For example if the input string is: "May 5 1992" your function 
should return "Tuesday"

# Assume that input was "May 5 1992"
day (d) = 5        # It is the 5th day
month (m) = 3      # (*** Count starts at March i.e March = 1, April = 2, ... 
January = 11, February = 12)
century (c) = 19   # the first two characters of the century
year (y) = 92      # Year is 1992 (*** if month is January or february 
decrease one year)
# Formula and calculation
day of the week (w) = (d + floor(2.6m - 0.2) - 2c + y + floor(y/4) + floor(c/4)) modulo 7
after calculation we get, (w) = 2

Count for the day of the week starts at Sunday, i.e Sunday = 0, Monday = 1, 
Tuesday = 2, ... Saturday = 6

"""

def day_of_the_week (x):
    import math
    x = x.split() #convert string to a list

    d = int(x[1]) # d is a day
    
    dict_months = {"January":11, "February":12, "March":1, "April":2, "May":3, 
                   "June":4, "July":5, "August":6, "September":7, "October":8, 
                   "November":9, "December":10}
    
    for i in dict_months.keys():
        if i == x[0]:
            m = dict_months[i] # m is month
            break
            
    str_cent = x[2]
    c_str = str_cent[0] + str_cent[1]
    y_str = str_cent[2] + str_cent[3]
    c = int(c_str) # c is century
    y = int(y_str) # y is year
    
    if m == 11 or m == 12:
        y = y - 1
    
    dict_weeks = {"Sunday": 0, "Monday": 1, "Tuesday": 2,
                "Wednesday": 3,"Thursday": 4,"Friday": 5,"Saturday": 6}
    
    #formula was given at the start of the assignement
    w = (d + math.floor(2.6*m - 0.2) - 2*c + y + math.floor(y/4) + math.floor(c/4)) % 7
    for i in dict_weeks.keys():
        if dict_weeks[i] == w:
            return i
    
print(day_of_the_week("November 11 1964"))