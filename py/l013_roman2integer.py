# coding: utf-8


class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        m = dict()
        m["I"] = 1
        m["V"] = 5
        m["X"] = 10
        m["L"] = 50
        m["C"] = 100
        m["D"] = 500
        m["M"] = 1000
        sumV = 0
        i = 0
        while i < len(s):
            current = s[i]
            if current == "V" or current == "L" or current == "D" or current == "M":
                sumV += m[current]
                i += 1
            elif current == "I":
                if i + 1 < len(s) and(s[i + 1] == "V" or s[i + 1] == "X"):
                    sumV += (m[s[i + 1]] - m[current])
                    i += 2
                else:
                    sumV += m[current]
                    i += 1
            elif current == "X":
                if i + 1 < len(s) and (s[i + 1] == "L" or s[i + 1] == "C"):
                    sumV += (m[s[i + 1]] - m[current])
                    i += 2
                else:
                    sumV += m[current]
                    i += 1
            elif current == "C":
                if i + 1 < len(s) and (s[i + 1] == "D" or s[i + 1] == "M"):
                    sumV += (m[s[i + 1]] - m[current])
                    i += 2
                else:
                    sumV += m[current]
                    i += 1
        return sumV


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV"))