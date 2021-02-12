# coding: utf-8


class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        if target == nums[-1]:
            return len(nums) - 1
        if target > nums[-1]:
            if nums[-1] > nums[0]:
                return -1
            for index, value in enumerate(nums):
                if value == target:
                    return index
                if index + 1 >= len(nums):
                    return -1
                if nums[index] > nums[index + 1]:
                    return -1
            return -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                return i
            if i == 0:
                return -1
            if nums[i] < nums[i - 1]:
                return -1
        return -1


if __name__ == '__main__':
    s = Solution()
    # print(s.search([4,5,6,7,0,1,2], 0))
    # print(s.search([4,5,6,7,0,1,2], 3))
    # print(s.search([1], 0))
    # print(s.search([4,5,6,7,0,1,2], 0))
    print(s.search([1], 2))
    print(s.search([1], 0))

