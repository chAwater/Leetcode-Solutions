# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1

        return idx
