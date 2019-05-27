# coding: utf-8


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        symbol_value = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                        (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        for s_v in symbol_value:
            v = s_v[0]
            s = s_v[1]
            index = num // v
            if index == 0:
                continue
            else:
                num %= v
            if s == "M":
                result += ("M" * index)
            elif s == "CM":
                result += "CM"
            elif s == "D":
                result += "D"
            elif s == "CD":
                result += "CD"
            elif s == "C":
                result += ("C" * index)
            elif s == "XC":
                result += "XC"
            elif s == "L":
                result += "L"
            elif s == "XL":
                result += "XL"
            elif s == "X":
                result += ("X" * index)
            elif s == "IX":
                result += "IX"
            elif s == "V":
                result += "V"
            elif s == "IV":
                result += "IV"
            else:
                result += ("I" * index)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(4))
    print(s.intToRoman(9))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
