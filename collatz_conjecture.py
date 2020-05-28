'''
Collatz Conjecture - Start with a number n > 1.
Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
'''
import time

def collatz_conjecture(num):
    '''
    Count number of steps it takes to reach one with use while loop
    num is number more 1
    '''
    count_n = 1
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3 + 1
        count_n += 1
    print(count_n)

def collatz_conjecture2(num, count_n):
    '''
    Count number of steps it takes to reach one with use recurse
    num is number more 1
    '''
    if num == 1:
        print(count_n)
        return num
    count_n += 1
    return collatz_conjecture2(num / 2 if num % 2 == 0 else num*3 + 1, count_n)

in_num = 1
while in_num <= 1:
    try:
        in_num = int(input('Please enter a number more than 1 '))
    except:
        print('Try again')

start_time = time.time()
collatz_conjecture(in_num)
print(time.time() - start_time)
start_time = time.time()
collatz_conjecture2(in_num, 1)
print(time.time() - start_time)
