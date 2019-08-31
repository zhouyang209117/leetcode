# coding: utf-8


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_result = 0
        for i in range(len(s)):
            if max_result >= len(s[i:]):
                break
            appearance = set()
            for a in s[i:]:
                if a not in appearance:
                    appearance.add(a)
                else:
                    break
            if len(appearance) > max_result:
                max_result = len(appearance)
        return max_result


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))