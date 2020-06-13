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

to_roman_table = [None]
from_roman_table = {}

def to_roman(num):
    '''convert integer to Roman numeral'''
    if not (0 < num < 5000):
        raise OutOfRangeError('number out of range (must be 1..4999)')
    if not isinstance(num, int):
        raise NotIntegerError('non-integers can not be converted')
    return to_roman_table[num]

def from_roman(string):
    '''convert Roman numeral to integer'''
    if not isinstance(string, str):
        raise InvalidRomanNumeralError('Input must be a string')
    if not string:
        raise InvalidRomanNumeralError('Input can not be blank') 
    if string not in from_roman_table:
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(string))
    return from_roman_table[string]

def build_lookup_tables():
    def to_roman(num):
        result = ''
        for numeral, integer in roman_numeral_map:
            if num >= integer:
                result = numeral
                num -= integer
                break
        if num > 0:
            result += to_roman_table[num]
        return result

    for integer in range(1, 5000):
        roman_numeral = to_roman(integer)
        to_roman_table.append(roman_numeral)
        from_roman_table[roman_numeral] = integer

build_lookup_tables()