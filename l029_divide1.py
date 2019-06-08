# coding: utf-8


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        same = True
        if divisor < 0 < dividend:
            divisor = -divisor
            same = False
        elif dividend < 0 < divisor:
            dividend = -dividend
            same = False
        result = 0
        max = 2147483648
        i = 0
        while i < max + 1:
            result += divisor
            if result > dividend:
                result = i
                break
            i += 1
        result = result if same else -result
        if result < -2147483648:
            return -2147483648
        elif result >= 2147483648:
            return 2147483647
        else:
            return result


if __name__ == '__main__':
    s = Solution()
    # print(s.divide(0, 3))
    print(s.divide(7, -3))
