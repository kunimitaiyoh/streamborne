import unittest
from streamborne.option import Option

class OptionTestCase(unittest.TestCase):
    def setUp(self):
        self.payload = 'foo'
        self.sut_present = Option.of(self.payload)
        self.sut_empty = Option.empty()

    def test_of(self):
        sut = Option.of(self.payload)
        self.assertTrue(sut.is_present())

        self.assertRaises(TypeError, lambda: Option.of(None))

    def test_of_nullable(self):
        sut = Option.of_nullable(self.payload)
        self.assertTrue(sut.is_present())

        sut = Option.of_nullable(None)
        self.assertTrue(sut.is_empty())

    def test_empty(self):
        sut = Option.empty()
        self.assertTrue(sut.is_empty())

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
