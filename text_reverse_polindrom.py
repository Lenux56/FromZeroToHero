'''
some task for text polindrom and reverse
'''
import re

def reverse_str():
    '''
    Enter a string and the program will reverse it and print it out
    '''
    in_str = input('Please, write a string for the reverse it: ')
    print(in_str[::-1])

def polindrom_str():
    '''
    Checks if the string entered by the user is a palindrome.
    That is that it reads the same forwards as backwards like “racecar”
    '''
    in_str = input('Please, write a string for check it as polindrom: ').lower()
    alpha_str = re.sub('[^\w]', '', in_str)
    print(alpha_str[:len(alpha_str)//2] == alpha_str[:len(alpha_str)//2:-1])
