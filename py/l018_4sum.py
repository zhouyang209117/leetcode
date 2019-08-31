# coding: utf-8


class Solution:
    def fourSum(self, nums: 'List[int]', target: int) -> 'List[List[int]]':
        result = list()
        if (not nums) or len(nums) < 4:
            return list(list())
        nums = sorted(nums)
        i = 0
        while i < len(nums) - 3:
            if nums[i] > 0 and nums[i] > target:
                return result
            j = i + 1
            while j < len(nums) - 2:
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                j += 1
                while j < len(nums) - 2 and nums[j] == nums[j - 1]:
                    j += 1
            i += 1
            while i < len(nums) - 3 and nums[i] == nums[i - 1]:
                i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    # print(s.fourSum([1, 1, 1, 1, -1, 3], 4))
    print(s.fourSum([1,-2,-5,-4,-3,3,3,5], -11))
