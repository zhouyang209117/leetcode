# coding: utf-8


def getCommonPrefix(a, b):
    minL = min(len(a), len(b))
    i = 0
    while i < minL and a[i] == b[i]:
        i += 1
    return a[: i]


class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0:
            return ""
        i = 1
        maxCommon = strs[0]
        while i < len(strs):
            currentCommon = getCommonPrefix(maxCommon, strs[i])
            if len(currentCommon) < len(maxCommon):
                maxCommon = currentCommon
            i += 1
        return maxCommon

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["dog","racecar","car"]))
