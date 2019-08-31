# coding: utf-8

class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        m = dict()
        for index, value in enumerate(nums):
            m[value] = index
        for index, value in enumerate(nums):
            if (target - value) in m and index != m[target - value]:
                return [index, m[target - value]]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 4, 5, 3], 6))