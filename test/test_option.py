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

    def test_get(self):
        self.assertEquals(self.payload, self.sut_present.get())
        self.assertRaises(TypeError, self.sut_empty.get())

    def test_if_present(self):
        called = False
        self.sut_present.if_present(lambda: called = True)
        self.assertTrue(called)

        called = False
        self.sut_empty.if_present(lambda: called = True)
        self.assertFalse(called)

    def test_filter(self):
        self.assertTrue(self.sut_present.filter(lambda x: len(x) > 0).is_present())
        self.assertTrue(self.sut_present.filter(lambda x: len(x) == 0).is_empty())
        self.assertTrue(self.sut_empty.filter(lambda x: True).is_empty())

    def test_map(self):
        mapper = len
        self.assertEqual(mapper(self.payload), self.sut_present.map(len).get())
        self.assertTrue(self.sut_empty.map(len).is_empty())
        self.assertTrue(self.sut_present.map(lambda x: None).is_empty())

    def test_flat_map(self):
        left = Option.of(3)
        right = Option.of(4)
        total = 3 + 4
        self.assertEqual(total, left.flat_map(lambda l: right.map(lambda r: l + r)).get())
        self.assertTrue(self.sut_empty.flat_map(lambda l: right.map(lambda r: l + r)).is_empty())
        self.assertTrue(left.flat_map(lambda l: self.sut_empty.map(lambda r: l + r)).is_empty())

    def test_or_else(self):
        another = "bar"
        self.assertEqual(self.sut_present.get(), self.sut_present.or_else(another))
        self.assertEqual(another, self.sut_empty.or_else(another))


    def test_or_else_get(self):
        another = "bar"
        self.assertEqual(self.sut_present.get(), self.sut_present.or_else_get(lambda: another))
        self.assertEqual(another, self.sut_empty.or_else_get(lambda: another))

    def test_or_else_throw(self):
        self.assertEqual(self.sut_present.get(), self.sut_present.or_else_throw(TypeError))
        self.assertRaises(TypeError, lambda: self.sut_empty.or_else_throw(TypeError))

    def test_or_none(self):
        self.assertEqual(self.sut_present.get(), self.sut_present.or_none())
        self.assertEqual(None, self.sut_empty.or_none())

    @unittest.skip
    def test_stream(self):
        self.assertSequenceEqual(list(self.sut_present.get()), self.sut_present.stream().list())
        self.assertSequenceEqual(list(), self.sut_empty.stream().list())
