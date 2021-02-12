# coding: utf-8


class Solution:
    def binary_sort(self, nums: 'List[int]', target: int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + int((right - left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def searchRange(self, nums: 'List[int]', target: int) -> 'List[int]':
        index = self.binary_sort(nums, target)
        if index == -1:
            return [-1, -1]
        start = end = index
        for i in range(index + 1, len(nums)):
            if nums[index] == nums[i]:
                end += 1
        for i in range(index - 1, -1, -1):
            if nums[index] == nums[i]:
                start -= 1
        return [start, end]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))
    print(s.searchRange([5,7,7,8,8,10], 6))
    print(s.searchRange([], 6))

