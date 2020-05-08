'''
unit test for generation e to nth digits
'''
import unittest
import math
from decimal import Decimal
import gen_e

class TestGenE(unittest.TestCase):
    """docstring for TestGenPi"unittest.TestGenPi __init__(self, arg):
       super(TestGenPi,unittest.TestGenPi.__init__()self.arg = arg"""
    def test_gen_e_20(self):
        '''
        generate e to 20th digits and check almost equal 10 digits
        '''
        result = gen_e.gen_e(20)
        self.assertAlmostEqual(result, Decimal(math.e), 10)

    def test_test_gen_e_100(self):
        '''
        generate e to 5000th digits and check almost equal 20 digits
        '''
        result = gen_e.gen_e(1000)
        self.assertAlmostEqual(result, Decimal(math.e), 20)

if __name__ == '__main__':
    unittest.main()
