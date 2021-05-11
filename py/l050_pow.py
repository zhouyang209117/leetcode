# coding: utf-8
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            result = x
            for i in range((-n) - 1):
                result *= x
            return 1 / result
        else:
            result = x
            for i in range(n - 1):
                result *= x
            return result


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.00000, 10))
    print(s.myPow(2.10000, 3))
    print(s.myPow(2.00000, -2))
    print(s.myPow(2.00000, 0))