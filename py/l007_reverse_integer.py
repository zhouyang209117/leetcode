# coding: utf-8

import math

class Solution:
    def reverse(self, x: 'int') -> 'int':
        maxV = math.pow(2, 31) - 1
        minV = 0 - math.pow(2, 31)
        negative = False
        if x < 0:
            negative = True
            x = 0 - x
        b = int(str(x)[::-1])
        if negative:
            b = 0 - b
        if b > maxV or b < minV:
            b = 0
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-1230))