from decimal import Decimal, getcontext
import math
from multiprocessing import Pool
import timeit

def gen_e(n_digits):
    getcontext().prec = n_digits+2
    return sum(1/Decimal(math.factorial(x)) for x in range(n_digits))

if __name__ == '__main__':
    N = 10**7 # total iterations
    
    P = 5      # number of processes
    p = Pool(P)
    getcontext().prec = N+2
    print(timeit.timeit(lambda: print(f'{Decimal(sum(p.map(gen_e, [N//P]*P))/Decimal(P)):0.10002d}'), number=10))
    p.close()
    p.join()
    print(f'{N} total iterations with {P} processes')
