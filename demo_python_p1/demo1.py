# for loop
# while loop
# sum of n numbers till user enters -999
num = int(input('Enter the numbers: '))
total = 0
while 1:
    
    if num == -999:
        break
    else:
        total += num
        num = int(input('Enter the numbers: '))
        

print(f"The sum of values is: {total}")