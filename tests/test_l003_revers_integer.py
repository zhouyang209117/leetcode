# coding: utf-8
import unittest


class TestReverseInteger(unittest.TestCase):
    def test_reverse_string(self):
        a = "abc"
        b = a[::-1]
        self.assertEqual(b, "cba")

    def test_integer2str(self):
        a = 1230
        print(int(str(a)[::-1]))