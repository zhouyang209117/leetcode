# coding: utf-8
import unittest


class TestReverseInteger(unittest.TestCase):
    def test_reverse_string(self):
        a = [9, 8, 2, 3, 7, 6, 4]
        # a = a[: 3].extend()
        a[:2] = sorted(a[:2])
        print(a)