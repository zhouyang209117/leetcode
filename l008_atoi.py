# coding: utf-8
import re

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip(" ")
        if not re.match("^(-?|\\+?)\\d+.*", str):
            return 0
        result = re.match("^(-?|\\+?)\\d+", str).group()
        if result.startswith("+"):
            result[1:]
        result = int(result)
        if result < -2147483648:
            return -2147483648
        if result > 2147483647:
            return 2147483647
        return result


if __name__ == '__main__':
    s = Solution()

    print(s.myAtoi("42"))
    print(s.myAtoi("   -42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("+1"))