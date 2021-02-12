# coding: utf-8
import unittest
from py.l032_longest_valid_parentheses import Solution


class TestReverseInteger(unittest.TestCase):
    def test_longest_valid_parentheses(self):
        s = Solution()
        self.assertEqual(s.longestValidParentheses(""), 0)
        self.assertEqual(s.longestValidParentheses("("), 0)
        self.assertEqual(s.longestValidParentheses(")"), 0)
        self.assertEqual(s.longestValidParentheses(")()())"), 4)