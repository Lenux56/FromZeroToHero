'''
Example merge sorting with generate list with random elements
'''
import random

def merge(a_list):
    '''
    Merge sort for incoming list with recurse for left and right part
    If len list is 1 list is sorted
    Сompare left and right part of list and put it in incoming list
    '''
    if len(a_list) == 1:
        return a_list

    if len(a_list)%2 == 0:
        mid = len(a_list)//2
    else:
        mid = len(a_list)//2 + 1
    left_a = a_list[:mid]
    right_a = a_list[mid:]
    merge(left_a)
    merge(right_a)
    i = j = k = 0
    while i < len(left_a) and j < len(right_a):
        if left_a[i] < right_a[j]:
            a_list[k] = left_a[i]
            i += 1
        else:
            a_list[k] = right_a[j]
            j += 1
        k += 1
    while i < len(left_a):
        a_list[k] = left_a[i]
        i += 1
        k += 1
    while j < len(right_a):
        a_list[k] = right_a[j]
        j += 1
        k += 1

b_list = [random.randrange(100) for x in range(15)]
print(b_list)
merge(b_list)
print(b_list)
