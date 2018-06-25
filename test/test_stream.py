import unittest
from streamborne.stream import Stream

class StreamTestCase(unittest.TestCase):
    def setUp(self):
        self.items = ['fred', 'wilma', 'barney', 'betty', 'pebbles', 'bamm-bamm', 'dino']

    # region intermediate operations
    def test_map(self):
        mapper = lambda x: len(x)
        actual = Stream.from_list(self.items).map(mapper).list()
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
