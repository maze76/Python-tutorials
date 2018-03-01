""" Write a function that calculates and returns the monthly payments for a loan.
This function accepts three parameters in the exact order (principal,
annual_interest_rate, duration):
r is the monthly interest rate (should be calculated by first dividing the
annual_interest_rate by 100 and then divide the result by 12 to make it monthly).
Notice that if the interest rate is equal to zero then the above equation will
give you a ZeroDivisionError
n is the total number of monthly payments for the entire duration of the loan
(Notice that n is equal to loan duration in years multiplied by 12).

"""


def monthly_payment_1(principal, annual_interest_rate, duration):
    n = duration * 12
    if annual_interest_rate != 0:
        r = (annual_interest_rate / 100) / 12
    else:
        r = principal / n
    return principal * ((r * (1 + r) ** n) / ((1 + r) ** n - 1))


# Your function for calculating remaining balance goes here
# This function accepts four parameters

def rem_loan_balance(principal, annual_interest_rate, duration, number_of_payments):
    p = number_of_payments
    n = duration * 12
    if annual_interest_rate != 0:
        r = (annual_interest_rate / 100) / 12
        remaining_loan_balance = principal * (((1 + r) ** n - (1 + r) ** p) / ((1 + r) ** n - 1))
    else:
        remaining_loan_balance = principal * (1 - (p / n))
    return remaining_loan_balance


# Your main program goes here
principal = float(input("Enter loan amount: "))
annual_interest_rate = float(input("Enter annual interest rate (percent): "))
duration = int(input("Enter loan duration in years: "))
monthly_payment = monthly_payment_1(principal, annual_interest_rate, duration)
print('LOAN AMOUNT:', int(principal), 'INTEREST RATE (PERCENT):', int(annual_interest_rate))
print('DURATION (YEARS):', duration, 'MONTHLY PAYMENT:', int(monthly_payment))
for year_number in range(1, 1 + duration):
    y = rem_loan_balance(principal, annual_interest_rate, duration, year_number * 12)
    print('YEAR:', year_number, 'BALANCE:', int(y), 'TOTAL PAYMENT', int(monthly_payment * year_number * 12))