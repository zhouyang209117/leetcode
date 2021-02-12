# coding: utf-8
import unittest
from py.l030_2 import Solution


class TestReverseInteger(unittest.TestCase):
    def test_reverse_string(self):
        s = Solution()
        r = s.match("aaabbbccc", ["aaa", "bbb", "ccc"], 3)
        r = s.match("aaabbccc", ["aaa", "aaa", "ccc"], 3)
        self.assertTrue(r)