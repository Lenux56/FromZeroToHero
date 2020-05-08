'''
some task for text polindrom and reverse
'''

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
    print(in_str.replace(' ', '') == in_str[::-1].replace(' ', ''))
