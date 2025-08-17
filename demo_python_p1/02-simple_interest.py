# Author: Vishwas
# Email: 
# Script to calculate simple interest v2.0
principal = float(input("Enter the principal amount: "))
time_in_months = int(input("Enter time in months: "))
rate_of_interest = float(input(r"Enter rate of interest in decimals (Ex: 7% is 0.07): "))
# Arithmetic operators : +,-,*,,/%,//
# Relational: <,>,<=,>=,==,!=
# Logical: and, or, not
simple_interest = (principal * time_in_months * rate_of_interest)/100 # si formula
# PEDMAS
# print('Simple Interest is: ')
# print(simple_interest)

# Various ways to print
# print('The Simple interest is: ', simple_interest)
# print('The Simple interest is: '+ str(simple_interest))
# print('The Simple interest is: %.2f'%(simple_interest))
# print('The Simple interest is: {0}'.format(simple_interest))
print(f'The simple interest is {simple_interest:.2f}')
