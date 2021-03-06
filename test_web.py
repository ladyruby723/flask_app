import unittest
from web import get_businesses

class BusinessesTestCase(unittest.TestCase):
	"""Tests for `web.py`"""
	
	def test_get_businesses(self):
		"""Verify that get_businesses returns a list of businesses for a set of expected param types"""
		self.assertTrue(get_businesses("Colorado Springs", "food"))


if __name__ == '__main__':
	unittest.main()
