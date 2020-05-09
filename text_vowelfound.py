'''
Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
'''
import re

def multi_re_find():
    '''
    search and count vowels
    '''
    phrase = input('Please, enter a phrase to find vowels and count it: ')
    while not phrase:
        print('Phrase is empty, please try again')
        phrase = input('Enter a phrase to find vowels and count it: ')

    print([{pattern:len(re.findall(pattern, phrase))} for pattern in 'aeyuio'])
