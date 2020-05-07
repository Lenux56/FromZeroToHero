import unittest
import bin_dec_convert

class TestConvert(unittest.TestCase):
	"""docstring for TestGenPi"unittest.TestCase __init__(self, arg):
		super(TestGenPi,unittest.TestCase.__init__()
		self.arg = arg"""
	def test_dec_to_bin(self):
			result = bin_dec_convert.dec_to_bin(22, [])
			self.assertEqual(result, '10110')
				
	def test_bin_to_dec(self):
		result = bin_dec_convert.bin_to_dec('10101')
		self.assertEqual(result, 21)

if __name__ == '__main__':
	unittest.main()