# coding: utf-8


class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        if not nums:
            return 0
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(s.removeDuplicates([]))

