import unittest
import roman_ex as roman

class ToRomanBadInput(unittest.TestCase):
    """docstring for ToRomanBadInput"""
    def test_too_large(self):
        '''to_roman should fail with large input'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 5000)

    def test_zero(self):
        '''to_romani fal with 0'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 0)

    def test_negative(self):
        '''to_roman fail with negative input'''
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, -1)

    def test_non_integer(self):
        '''to_roman fail with non-integer input'''
        self.assertRaises(roman.NotIntegerError, roman.to_roman, 1.0)

class FromRomanBadInput(unittest.TestCase):
    """docstring for FromRomanBadInput"""
    def test_too_many_repeated_numerals(self):
        '''from_roman fail with to many repeated numerals'''
        for string in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, string)

    def test_repeated_pairs(self):
        '''from_roman should fail with repeated pairs of numerals'''
        for string in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, string)

    def tes_malformed_antecedents(self):
        '''from_roman should fail with malformed antecedents'''
        for string in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIX', 'MCMC',
                       'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, string)

    def testBlank(self):
        '''from_roman should fail with blank string'''
        self.assertRaises(roman.InvalidRomanNumeralError, roman.from_roman, '')

if __name__ == '__main__':
    unittest.main()
