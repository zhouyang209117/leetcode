# coding: utf-8


def get_numbers(digits, num2letter):
    total = 1
    numbers = list()
    for s in range(len(digits) - 1, -1, -1):
        total *= len(num2letter[digits[s]])
        if s == len(digits) - 1:
            numbers.insert(0, 1)
        else:
            numbers.insert(0, numbers[0] * len(num2letter[digits[s + 1]]))
    return numbers, total


class Solution:
    def letterCombinations(self, digits: str) -> 'List[str]':
        if not digits:
            return list()
        num2letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        numbers, total = get_numbers(digits, num2letter)
        result = list()
        for i in range(total):
            r = ""
            tmp_i = i
            for index, num in enumerate(numbers):
                r += num2letter[digits[index]][tmp_i // num]
                tmp_i %= num
            result.append(r)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations(""))
