'''
unit test to bin_dec_convert.py
'''
import unittest
import bin_dec_convert

class TestConvert(unittest.TestCase):
    """docstring for TestGenPi"unittest.TestCase __init__(self, arg):
    	super(TestGenPi,unittest.TestCase.__init__()
    	self.arg = arg"""
    def test_dec_to_bin(self):
        '''
        check 22 in binary, waiting output 10110
        '''
        result = bin_dec_convert.dec_to_bin(22, [])
        self.assertEqual(result, '10110')

    def test_bin_to_dec(self):
        '''
        check 10101 in decimal, waiting output 21
        '''
        result = bin_dec_convert.bin_to_dec('10101')
        self.assertEqual(result, 21)

if __name__ == '__main__':
    unittest.main()
