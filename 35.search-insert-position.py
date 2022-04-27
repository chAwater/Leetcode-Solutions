# https://leetcode-cn.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        length = len(nums)
        if length <= 3:
            if target in nums:
                for i,v in enumerate(nums):
                    if target == v:
                        return i
            else:
                for i,v in enumerate(nums):
                    if target > v:
                        return i+1

                return i+2
    
        ls = length // 2

        if nums[ls] > target:
            return self.searchInsert(nums[:ls+1], target)
        elif nums[ls] < target:
            rs = self.searchInsert(nums[ls:], target)
            return ls + rs + 1
        else:
            rs = []
            for i,v in enumerate(nums):
                if target == v:
                    return i
