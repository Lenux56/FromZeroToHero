'''
generation e to nth digits
'''
from decimal import Decimal, getcontext
import math

def gen_e(n_digits):
    '''
    In the special case where x = 1 or −1, we have:
    '''
    getcontext().prec = n_digits + 2
    return sum(1/Decimal(math.factorial(x)) for x in range(n_digits))

def check_input():
    '''
    Check the input number and return it if it`s ok
    '''
    while True:
        try:
            digits = int(input('Enter a number of decimal places to e '))
            if digits >= 1000000:
                print('Number is too large, please try again')
                continue
            elif digits < 1:
                print('Number is too small, please try again')
                continue
            else:
                break
        except:
            print('The input is wrong, please try again')
            continue
    return digits

print(gen_e(check_input()))
