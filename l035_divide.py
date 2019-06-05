# coding: utf-8


class Solution:
    def searchInsert(self, nums: 'List[int]', target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
            if i + 1 < len(nums) and nums[i] < target <= nums[i + 1]:
                return i + 1
        return len(nums)


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
