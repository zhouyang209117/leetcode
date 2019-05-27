# coding: utf-8


class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            return False
        reverse_x = int(str(x)[::-1])
        return reverse_x == x


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(1010))