# coding: utf-8


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        result = list(list())
        keyes = set()
        value_index = dict()
        for index, v in enumerate(nums):
            value_index[v] = index
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums):
                if i == j:
                    continue
                v3 = 0 - v1 - v2
                if v3 in value_index and value_index[v3] != i and value_index[v3] != j:
                    tmp_list = sorted([v1, v2, v3])
                    tmp_str_list = [str(current_num) for current_num in tmp_list]
                    key = "".join(tmp_str_list)
                    if key not in keyes:
                        result.append(tmp_list)
                        keyes.add(key)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))