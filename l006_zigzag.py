# coding: utf-8

import math


def get_coord(row_num, part_index, offset):
    part_col = row_num - 1
    if offset < row_num:
        return offset, part_index * part_col
    if offset >= row_num:
        return 2 * row_num - offset - 2, part_index * part_col + (offset - row_num) + 1


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        numCols = math.ceil(len(s) / (2 * numRows - 2)) * (2 * numRows - 2)
        m = [[""] * numCols for _ in range(numRows)]
        result = ""
        for i in range(len(s)):
            part_index = math.floor(i / (2 * numRows - 2))
            offset = i % (2 * numRows - 2)
            x, y = get_coord(numRows, part_index, offset)
            m[x][y] = s[i]
        for i in range(numRows):
            for j in range(numCols):
                if m[i][j] != "":
                    result += m[i][j]
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 2))