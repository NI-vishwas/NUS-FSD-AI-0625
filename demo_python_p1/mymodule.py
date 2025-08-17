
def is_even(num):
    return num % 2 == 0


if __name__ == '__main__':
    num = int(input('Enter a number: '))
    if is_even(num):
        print('It is an even number')
    else:
        print('It is not a even number')
