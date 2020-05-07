import unittest
import gen_pi
import math
from decimal import Decimal

class TestGenPi(unittest.TestCase):
	"""docstring for TestGenPi"unittest.TestGenPi __init__(self, arg):
		super(TestGenPi,unittest.TestGenPi.__init__()
		self.arg = arg"""
	def test_gen_pi_20(self):
			result = gen_pi.gen_pi(20)
			self.assertAlmostEqual(result, Decimal(math.pi), 10)
	
	def test_test_gen_pi_100(self):
		result = gen_pi.gen_pi(5000)
		self.assertAlmostEqual(result, Decimal(math.pi), 20)

if __name__ == '__main__':
	unittest.main()