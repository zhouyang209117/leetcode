# coding: utf-8


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        value_symbol = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
                        10: "X", 9: "IX", 5: "V", 4: "IV", 1:"I"}
        for v in values:
            index = num // v
            if index != 0:
                result += (value_symbol[v] * index)
                num %= v
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(4))
    print(s.intToRoman(9))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
