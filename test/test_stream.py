import unittest
from streamborne.stream import Stream

class StreamTestCase(unittest.TestCase):
    def setUp(self):
        self.items = ['fred', 'wilma', 'barney', 'betty', 'pebbles', 'bamm-bamm', 'dino']

    def test_map(self):
        mapper = lambda x: len(x)
        actual = Stream.from_list(self.items).map(mapper).as_list()
        expected = list(map(mapper, self.items))
        self.assertListEqual(actual, expected)
