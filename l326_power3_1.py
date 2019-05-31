# coding: utf-8
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0 or n % 3 != 0:
            return False
        else:
            n = n // 3
            return self.isPowerOfThree(n)


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(27))
    print(s.isPowerOfThree(0))
    print(s.isPowerOfThree(9))
    print(s.isPowerOfThree(45))
    print(s.isPowerOfThree(1))
    print(s.isPowerOfThree(3))