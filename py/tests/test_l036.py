# coding: utf-8
import unittest
from py.l036_valid_sudoku import same_area


class TestArea(unittest.TestCase):
    def test1(self):
        inita = same_area(0, 0)
        self.assertTrue((0, 1) in inita)
        self.assertTrue((0, 2) in inita)
        self.assertTrue((1, 0) in inita)
        self.assertTrue((1, 1) in inita)
        self.assertTrue((1, 2) in inita)
        self.assertTrue((2, 0) in inita)
        self.assertTrue((2, 1) in inita)
        self.assertTrue((2, 2) in inita)
        self.assertEqual(8, len(inita))

    def test2(self):
        inita = same_area(0, 8)
        self.assertTrue((0, 6) in inita)
        self.assertTrue((0, 7) in inita)
        self.assertTrue((1, 6) in inita)
        self.assertTrue((1, 7) in inita)
        self.assertTrue((1, 8) in inita)
        self.assertTrue((2, 6) in inita)
        self.assertTrue((2, 7) in inita)
        self.assertTrue((2, 8) in inita)
        self.assertEqual(8, len(inita))

    def test3(self):
        inita = same_area(8, 0)
        self.assertTrue((6, 0) in inita)
        self.assertTrue((6, 1) in inita)
        self.assertTrue((6, 2) in inita)
        self.assertTrue((7, 0) in inita)
        self.assertTrue((7, 1) in inita)
        self.assertTrue((7, 2) in inita)
        self.assertTrue((8, 1) in inita)
        self.assertTrue((8, 2) in inita)
        self.assertEqual(8, len(inita))


    def test4(self):
        inita = same_area(8, 8)
        self.assertTrue((6, 6) in inita)
        self.assertTrue((6, 7) in inita)
        self.assertTrue((6, 8) in inita)
        self.assertTrue((7, 6) in inita)
        self.assertTrue((7, 7) in inita)
        self.assertTrue((7, 8) in inita)
        self.assertTrue((8, 6) in inita)
        self.assertTrue((8, 7) in inita)
        self.assertEqual(8, len(inita))