import unittest
from web import get_businesses

class BusinessesTestCase(unittest.TestCase):
	"""Tests for `web.py`"""
	
	def test_get_businesses(self):
		"""Do the params 'Colorado Springs', 'food' return a list of businesses?"""
		self.assertTrue(get_businesses("Colorado Springs", "food"))


if __name__ == '__main__':
	unittest.main()
