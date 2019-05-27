# coding: utf-8


import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        r = re.match(p, s)
        if r is None:
            return False
        return r.group() == s


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aa", "a"))
    print(s.isMatch("aa", "a*"))
    print(s.isMatch("ab", ".*"))
    print(s.isMatch("aab", "c*a*b"))
    print(s.isMatch("mississippi", "mis*is*p*."))