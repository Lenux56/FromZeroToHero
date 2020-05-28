'''
Example for buuble sorting with generate list with random elements 
'''
import random

def bubble(a_list):
    '''
    buuble sort for incomin list with stop if list is sorted
    '''
    swap = False
    for i in range(len(a_list)-1):
        for j in range(len(a_list)-1-i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                swap = True
        if not swap:
            break

bad_list = [random.randrange(100) for x in range(15)]
print(bad_list)
bubble(bad_list)
print(bad_list)
