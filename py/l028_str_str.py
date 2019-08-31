# coding: utf-8


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def match(index):
            if len(haystack[index:]) < len(needle):
                return False, -1
            tmp = index
            for j in range(len(needle)):
                if haystack[tmp] != needle[j]:
                    return False, -1
                else:
                    tmp += 1
            return True, index
        if not needle:
            return 0
        for i in range(len(haystack)):
            success, index = match(i)
            if success:
                return index
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("a", "a"))
    print(s.strStr("hello", "ll"))
    print(s.strStr("aaaaa", "bba"))
