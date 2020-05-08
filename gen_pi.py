'''
generation pi to nth digits
'''
from decimal import Decimal, getcontext

def gen_pi(n_digits):
    '''
    The Chudnovsky algorithm is a fast method for calculating the digits of π,
    based on Ramanujan’s π formulae.
    https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    '''
    getcontext().prec = n_digits+2
    m, l, x, k, s = 1, 13591409, 1, 6, 13591409
    try:
        for i in range(1, n_digits):
            m *= (k**3 - 16*k)/Decimal((i + 1)**3)
            l += 545140134
            x *= Decimal(-262537412640768000)
            k += 12
            s += Decimal(m*l)/Decimal(x)
    except MemoryError:
        return 'Memory is out'
    except OverflowError:
        return 'Memory is out'
    else:
        return 426880*Decimal(10005**0.5)/Decimal(s)

def check_input():
    '''
    Check the input number and return it if it`s ok
    '''
    while True:
        try:
            digits = int(input('Enter a number of decimal places to pi '))
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

print(gen_pi(check_input()))
