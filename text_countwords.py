'''
Count Words in a String - Counts the number of individual words in a string.
For added complexity read these strings in from a text file and generate a summary.
'''

def find_word():
    '''
    search and count words in text file
    '''

    with open('blabla.txt') as file:
        read_data = file.read()

        
    file.closed
    word_list = read_data.split()
    print([{x:word_list.count(x) for x in word_list}])
