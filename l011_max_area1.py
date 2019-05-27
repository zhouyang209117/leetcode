# coding: utf-8


class Solution:
    def maxArea(self, height: 'List[int]') -> int:
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                h = min(height[i], height[j])
                tmp_area = h * (j - i)
                max_area = tmp_area if tmp_area > max_area else max_area
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
