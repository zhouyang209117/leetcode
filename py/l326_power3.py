# coding: utf-8
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(27))
    print(s.isPowerOfThree(0))
    print(s.isPowerOfThree(9))
    print(s.isPowerOfThree(45))
    print(s.isPowerOfThree(1))
    print(s.isPowerOfThree(3))