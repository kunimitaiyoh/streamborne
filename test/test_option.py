import unittest
from streamborne.option import Option

class OptionTestCase(unittest.TestCase):
    def setUp(self):
        self.payload = 'foo'
        self.sut_present = Option(self.payload)
        self.sut_empty = Option(None)

    @unittest.skip
    def test_of(self):
        None

    @unittest.skip
    def test_of_nullable(self):
        None

    @unittest.skip
    def test_empty(self):

    def test_is_present(self):
        self.assertTrue(self.sut_present.is_present())
        self.assertFalse(self.sut_empty.is_present())

    def test_is_empty(self):
        self.assertFalse(self.sut_present.is_empty())
        self.assertTrue(self.sut_empty.is_empty())

    @unittest.skip
    def test_if_present(self):
        None

    @unittest.skip
    def test_filter(self):
        None

    @unittest.skip
    def test_map(self):
        None

    @unittest.skip
    def test_flat_map(self):
        None

    @unittest.skip
    def test_or_else(self):
        None

    @unittest.skip
    def test_or_else_get(self):
        None

    @unittest.skip
    def test_or_else_throw(self):
        None

    @unittest.skip
    def test_or_none(self):
        None

    @unittest.skip
    def test_stream(self):
        None
