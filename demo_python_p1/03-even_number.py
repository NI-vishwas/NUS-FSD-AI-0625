num = int(input('Enter a number: '))
if num % 2 == 0:
    print('It is an even number')
    print('I am still inside if block')
# elif condn:
#     pass
else:
    print('I am inside Else Block')
    print('It is not a even number')
print('I am outside the if block')