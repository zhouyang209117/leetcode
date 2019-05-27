# coding: utf-8


class Solution:
    def maxArea(self, height: 'List[int]') -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            tmp_area = (j - i) * min(height[i], height[j])
            max_area = tmp_area if tmp_area > max_area else max_area
            if height[i] < height[j]:
                h = height[i]
                while height[i] <= h and i < j:
                    i += 1
            else:
                h = height[j]
                while height[j] <= h and i < j:
                    j -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
