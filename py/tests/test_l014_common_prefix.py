# coding: utf-8
import unittest

def getCommonPrefix(a, b):
    minL = min(len(a), len(b))
    i = 0
    while i < minL and a[i] == b[i]:
        i += 1
    return a[: i]


class TestCommonPrefix(unittest.TestCase):
    def test1(self):
        a = "aabbcc"
        b = ""
        print(getCommonPrefix(a, b))