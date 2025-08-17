# Author: Vishwas
# Email: 
# Script to calculate simple interest v1.0
principal = 100000
time_in_months = 36
rate_of_interest = 0.07
# Arithmetic operators : +,-,*,,/%,//
# Relational: <,>,<=,>=,==,!=
# Logical: and, or, not
simple_interest = (principal * time_in_months * rate_of_interest)/100 # si formula
# PEDMAS
# print('Simple Interest is: ')
# print(simple_interest)

# Various ways to print
print('The Simple interest is: ', simple_interest)
print('The Simple interest is: '+ str(simple_interest))
print('The Simple interest is: %.2f'%(simple_interest))
print('The Simple interest is: {0}'.format(simple_interest))
print(f'The simple interest is {simple_interest:.2f}')
