# mortgage.py
"""
    Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with
    Guido's Mortgage, Stock Investment, and Bitcoin trading corporation.
    The interest rate is 5% and the monthly payment is $2684.11
"""
# Exercise 1.7
principal = 500_000
rate = 0.05
payment = 2684.11
total_paid = 0

# the rate is annual so we need to break it down to montly
rate_per_month = rate / 12
first_year = 12
months = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_extra_payment = payment + extra_payment

# We want to modify this so we can put a start month to pay the extra $1000 and an end month
while principal > 0:
    payment_per_month = payment
    principal_with_monthly_interest = principal * (1 + rate_per_month)
        
    if principal_with_monthly_interest < payment_per_month:
        payment_per_month = principal_with_monthly_interest
    elif months >= extra_payment_start_month and months <= extra_payment_end_month:
        payment_per_month = total_extra_payment
    else:
        payment_per_month = payment
    
    principal = principal_with_monthly_interest - payment_per_month
    total_paid += payment_per_month
    print(f'{months} {total_paid} {principal}')
    months += 1
    


