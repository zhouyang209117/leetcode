# coding: utf-8
import unittest
from l006_zigzag import get_coord


class TestCommonPrefix(unittest.TestCase):
    def test1(self):
        (x, y) = get_coord(4, 0, 0)
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        (x, y) = get_coord(4, 0, 3)
        self.assertEqual(x, 3)
        self.assertEqual(y, 0)
        (x, y) = get_coord(4, 0, 5)
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)
        (x, y) = get_coord(4, 1, 1)
        self.assertEqual(x, 1)
        self.assertEqual(y, 3)
        (x, y) = get_coord(4, 1, 4)
        self.assertEqual(x, 2)
        self.assertEqual(y, 4)