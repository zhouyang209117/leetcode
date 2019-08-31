# coding: utf-8


class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> float:
        total_num = len(nums1) + len(nums2)
        if total_num == 1:
            return float(nums1[0]) if len(nums1) == 1 else float(nums2[0])
        a = 0
        b = 0
        end = int(total_num / 2) if (total_num % 2 == 0) \
            else int((total_num - 1) / 2)
        nums1_last = False
        for cnt in range(end):
            if a < len(nums1) and b < len(nums2):
                if nums1[a] < nums2[b]:
                    a += 1
                    nums1_last = True
                else:
                    b += 1
                    nums1_last = False
                continue
            if a < len(nums1):
                a += 1
                nums1_last = True
            if b < len(nums2):
                b += 1
                nums1_last = False
        add1 = nums1[a - 1] if nums1_last else nums2[b - 1]
        if a < len(nums1) and b < len(nums2):
            add2 = nums1[a] if nums1[a] < nums2[b] else nums2[b]
        elif a < len(nums1):
            add2 = nums1[a]
        else:
            add2 = nums2[b]
        return (add1 + add2) / 2 if total_num % 2 == 0 else float(add2)


if __name__ == '__main__':
    nums1 = [2]
    nums2 = []
    s = Solution()
    print(s.findMedianSortedArrays(nums1, nums2))