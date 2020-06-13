'''
There is only one correct way to represent a particular number as a Roman numeral.
The converse is also true: if a string of characters is a valid Roman numeral,
it represents only one number (that is, it can only be interpreted one way).
There is a limited range of numbers that can be expressed as Roman numerals,
specifically 1 through 3999. The Romans did have several ways of expressing larger numbers,
for instance by having a bar over a numeral to represent that its normal value should be multiplied
by 1000. For the purposes of this chapter, let’s stipulate that Roman numerals go from 1 to 3999.
There is no way to represent 0 in Roman numerals.
There is no way to represent negative numbers in Roman numerals.
There is no way to represent fractions or non-integer numbers in Roman numerals.
'''
import re

class OutOfRangeError(ValueError):
    pass
class NotIntegerError(ValueError):
    pass
class InvalidRomanNumeralError(ValueError):
    pass

roman_numeral_pattern = re.compile('''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    ''', re.VERBOSE)

roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))

def to_roman(num):
    '''convert integer to Roman numeral'''
    if not (0 < num < 4000):
        raise OutOfRangeError('number out of range (must be 1..3999)')
    if not isinstance(num, int):
        raise NotIntegerError('non-integers can not be converted')

    result = ''
    for numeral, integer in roman_numeral_map:
        while num >= integer:
            result += numeral
            num -= integer
    return result

def from_roman(string):
    '''convert Roman numeral to integer'''
    if not roman_numeral_pattern.search(string):
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(string))

    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while string[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
