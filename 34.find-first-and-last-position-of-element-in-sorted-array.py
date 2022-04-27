# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        if length <= 3:
            if target in nums:
                rs = []
                for i,v in enumerate(nums):
                    if target == v:
                        rs.append(i)
                return [rs[0], rs[-1]]
            else:
                return [-1, -1]

        ls = length // 2

        if nums[ls] > target:
            return self.searchRange(nums[:ls], target)
        elif nums[ls] < target:
            rs = self.searchRange(nums[ls:], target)
            if rs[0] != -1:
                return [ls + r for r in rs]
            else:
                return rs
        else: 
            rs = []
            for i,v in enumerate(nums):
                if target == v:
                    rs.append(i)
            return [rs[0], rs[-1]]

        
