# https://leetcode-cn.com/problems/two-sum/

from typing import List


class Solution1:
    '''
    Date: 2022.03.30
    Pass/Error/Bug: 2/3/5
    执行用时：28.0 ms, 在所有 Python3 提交中击败了 98.42% 的用户
    内存消耗：16.1 MB, 在所有 Python3 提交中击败了 17.90% 的用户
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Build hash for index
        v_dict = {}
        for i, v in enumerate(nums):
            if v in v_dict:
                last = v_dict[v]
                if type(last) == list:
                    v_dict[v] += [i]
                else:
                    v_dict[v] = [last, i]
            else:
                v_dict[v] = i

        for v1, idxs1 in v_dict.items():
            v2 = target - v1
            if v1 == v2:
                if (type(idxs1) == list) and (len(idxs1) >= 2):
                    return idxs1[0], idxs1[1]
            elif v2 in v_dict:
                idxs2 = v_dict[v2]
                idx1 = idxs1[0] if type(idxs1) == list else idxs1
                idx2 = idxs2[0] if type(idxs2) == list else idxs2
                return idx1, idx2
            else:
                continue


class Solution2:
    '''
    Date: 2022.03.30
    Pass/Error/Bug: 1/3/0
    执行用时：4.192 s, 在所有 Python3 提交中击败了  6.52% 的用户
    内存消耗：15.6 MB, 在所有 Python3 提交中击败了 63.55% 的用户
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = nums[i]
            for j in range(len(nums[i+1:])):
                b = nums[i+1+j]
                if target == a+b:
                    return i, i+1+j
