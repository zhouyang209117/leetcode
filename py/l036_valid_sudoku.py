# coding: utf-8
from typing import List


def same_area(x, y):
    mod_x = x % 3
    mod_y = y % 3
    left_x = int(x / 3)
    left_y = int(y / 3)
    a = list()
    a.append((0, 0))
    a.append((0, 1))
    a.append((0, 2))
    a.append((1, 0))
    a.append((1, 1))
    a.append((1, 2))
    a.append((2, 0))
    a.append((2, 1))
    a.append((2, 2))
    a.remove((mod_x, mod_y))
    b = list()
    for x in a:
        b.append((int(left_x * 3 + x[0]), int(left_y * 3 + x[1])))
    return b



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row_index, row in enumerate(board):
            for col_index, cell in enumerate(row):
                pass
        return True

# if __name__ == '__main__':
#     s = Solution()
#     a = list()
#     a.append("aaa")
#     a.append("bbb")
#     b = list()
#     b.append(a)
#     print(s.isValidSudoku(b))
