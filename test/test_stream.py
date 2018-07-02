import unittest
from streamborne.stream import Stream
from streamborne.option import Option

mapper = lambda x: len(x)
predicate = lambda x: len(x) == 5

class StreamTestCase(unittest.TestCase):

    def setUp(self):
        self.items = ['fred', 'wilma', 'barney', 'betty', 'pebbles', 'bamm-bamm', 'dino']

    def from_list(self):
        return Stream.from_list(self.items)

    # region intermediate operations
    def test_filter(self):
        actual = self.from_list().filter(predicate).list()
        expected = list(filter(predicate, self.items))
        self.assertListEqual(actual, expected)

    def test_map(self):
        actual = self.from_list().map(mapper).list()
        expected = list(map(mapper, self.items))
        self.assertListEqual(actual, expected)
    # endregion
    # region terminal operations for aggregation
    # endregion
    # region terminal operations for collecting
    # endregion
    # region private functions
    # endregion
    # region factory methods
    # endregion
