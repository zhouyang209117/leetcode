# coding: utf-8
from itertools import combinations, permutations


class Solution:
    def findSubstring(self, s: str, words: 'List[str]') -> 'List[int]':
        if (not s) or (not words):
            return list()
        subStr = set("".join(a) for a in permutations(words, len(words)))
        ans = list()
        for sub in subStr:
            index = s.find(sub)
            while index != -1:
                ans.append(index)
                index = s.find(sub, index + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
    print(s.findSubstring("foobarfoobar", ["foo", "bar"]))
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    print(s.findSubstring("", []))
    print(s.findSubstring("a", []))
    # "wordgoodgoodgoodbestword"
    # ["word","good","best","good"]