# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution1:
    '''
    Date: 2022.04.28
    Pass/Error/Bug: 1/3/0
    执行用时：  24 ms, 在所有 Python3 提交中击败了 99.95% 的用户
    内存消耗：16.2 MB, 在所有 Python3 提交中击败了  9.60% 的用户
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp_i = 1

        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                nums[tmp_i-1] = nums[i]
                tmp_i += 1

        if tmp_i == 1:
            return tmp_i
        else:
            return tmp_i-1
