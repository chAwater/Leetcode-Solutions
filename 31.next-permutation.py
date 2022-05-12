# https://leetcode-cn.com/problems/next-permutation/

from typing import List


class Solution1:
    '''
    Date: 2022.05.13
    Pass/Error/Bug: 1/4/0
    执行用时：  32 ms, 在所有 Python3 提交中击败了 91.66% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 24.52% 的用户
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        for idx1 in range(length-1, 0, -1):
            if nums[idx1] <= nums[idx1-1]:
                continue

            for idx2 in range(length-1, idx1-1, -1):
                if nums[idx2] > nums[idx1-1]:
                    break

            nums[idx1-1], nums[idx2] = nums[idx2], nums[idx1-1]
            nums[idx1:] = sorted(nums[idx1:])

            return

        nums.reverse()
