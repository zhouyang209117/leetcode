# coding: utf-8


class Solution:
    def get_down(self, nums):
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1
        return i - 1

    def get_small(self, nums, index):
        i = len(nums) - 1
        while i > index:
            if nums[index] < nums[i]:
                return i
            i -= 1

    def nextPermutation(self, nums: 'List[int]') -> None:
        if not nums:
            return
        index = self.get_down(nums)
        if index == -1:
            nums.sort()
            return
        small_index = self.get_small(nums, index)
        tmp = nums[small_index]
        nums[small_index] = nums[index]
        nums[index] = tmp
        nums[index + 1:] = sorted(nums[index + 1:])


if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3]
    s.nextPermutation(a)
    print(a)
    a = [3, 2, 1]
    s.nextPermutation(a)
    print(a)
    a = [1, 1, 5]
    s.nextPermutation(a)
    print(a)
    a = [0, 1, 3, 4, 2]
    s.nextPermutation(a)
    print(a)