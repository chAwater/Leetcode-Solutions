# https://leetcode-cn.com/problems/remove-element/

from typing import List


class Solution1:
    '''
    Date: 2022.04.28
    Pass/Error/Bug: 1/0/0
    执行用时：  40 ms, 在所有 Python3 提交中击败了 40.39% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 14.20% 的用户
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1

        return idx
