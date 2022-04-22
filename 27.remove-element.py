# https://leetcode-cn.com/problems/remove-element/

from typing import List


class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1

        return idx
