# coding: utf-8


def test_result(val, divisor):
    i = 0
    while i < 31:
        if (divisor << i) == val:
            return i
        elif (divisor << i) > val:
            return i - 1
        i += 1
    return i


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        same = True
        if divisor < 0 < dividend:
            divisor = -divisor
            same = False
        elif dividend < 0 < divisor:
            dividend = -dividend
            same = False
        tmp_dividend = abs(dividend)
        ans = 0
        while tmp_dividend != 0:
            if tmp_dividend < abs(divisor):
                break
            move_bit = test_result(tmp_dividend, abs(divisor))
            ans += (1 << move_bit)
            tmp_dividend -= ((1 << move_bit) * abs(divisor))
        ans = ans if same else -ans
        return ans if (-2147483648 <= ans <= 2147483647) else 2147483647


if __name__ == '__main__':
    s = Solution()
    # print(s.divide(0, -3))
    print(s.divide(-2147483648, -1))
    print(s.divide(-2147483648, 1))