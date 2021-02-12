# coding: utf-8


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        maxLen = 0
        for i in range(2, n + 1):
            if s[i - 1] == ")":
                if s[i - 2] == "(":
                    dp[i] = dp[i - 2] + 2
                    maxLen = max(maxLen, dp[i])
                elif (i - 2 - dp[i - 1] >= 0) and s[i - 2 - dp[i - 1]] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
                    maxLen = max(maxLen, dp[i])
        return maxLen


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses("(()))())("))