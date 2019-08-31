# coding: utf-8


class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: int) -> int:
        start = True
        nums = sorted(nums)
        result = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                error = total - target
                if start:
                    closest = error
                    result = total
                    start = False
                if abs(closest) > abs(error):
                    closest = error
                    result = total
                if error > 0:
                    right -= 1
                elif error < 0:
                    left += 1
                else:
                    return result
        return result


if __name__ == '__main__':
    s = Solution()
    # print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([0, 1, 2], 3))