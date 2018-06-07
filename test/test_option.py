import unittest
from streamborne.option import Option

class OptionTestCase(unittest.TestCase):
    def setUp(self):
        self.payload = 'foo'
        self.sut_present = Option(self.payload)
        self.sut_empty = Option(None)

    def test_is_present_of_present_be_true(self):
        self.assertTrue(self.sut_present.is_present())

    def test_is_present_of_empty_be_false(self):
        self.assertFalse(self.sut_empty.is_present())
