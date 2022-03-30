from typing import List

class Solution1:
    '''
    Date: 2022.03.30
    执行用时：40 ms, 在所有 Python3 提交中击败了 72.05% 的用户
    内存消耗：16.8 MB, 在所有 Python3 提交中击败了 5.00% 的用户
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Build hash for index
        v_dict = {}
        for i, v in enumerate(nums):
            if v in v_dict:
                v_dict[v].append(i)
            else:
                v_dict[v] = [i]

        for v1, idxs1 in v_dict.items():
            v2 = target - v1
            if v1 == v2:
                if len(idxs1)>=2:
                    return idxs1[0], idxs1[1]
            elif v2 in v_dict:
                idxs2 = v_dict[v2]
                return idxs1[0], idxs2[0]
            else:
                continue
