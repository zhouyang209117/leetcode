# coding: utf-8


class Solution:
    def removeElement(self, nums: 'List[int]', val: int) -> int:
        j = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                cnt += 1
                nums[j] = nums[i]
                j += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    a = [1]
    print(s.removeElement(a, 1))
    print(a)

