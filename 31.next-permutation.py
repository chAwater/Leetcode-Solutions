# https://leetcode-cn.com/problems/next-permutation/

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        for idx in range(length-1, 0, -1):
            if nums[idx] > nums[idx-1]:
                nums[idx-1], nums[idx] = nums[idx], nums[idx-1]
                nums[idx:] = sorted(nums[idx:])
                return
        nums.reverse()
