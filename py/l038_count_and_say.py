# coding: utf-8


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        last = "1"
        for i in range(2, n + 1):
            while j < len(last):
                pass





if __name__ == '__main__':
    s = Solution()
    # print(s.divide(0, 3))
    print(s.searchInsert([1,3,5,6], 5))
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 7))
    print(s.searchInsert([1,3,5,6], 0))
    print(s.searchInsert([1], 2))
    print(s.searchInsert([1], 0))
    print(s.searchInsert([], 0))
