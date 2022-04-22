# https://leetcode-cn.com/problems/next-permutation/

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length):
            if nums[length-i-2] < nums[length-i-1]:
                nums[length-i-1], nums[length-i-2] = nums[length-i-2], nums[length-i-1]
                return

        nums.reverse()
