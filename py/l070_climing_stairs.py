# coding: utf-8
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        result = 0
        for i in range(2, n):
            result = a + b
            a = b
            b = result
        return result


if __name__ == '__main__':
    print(Solution().climbStairs(3))
