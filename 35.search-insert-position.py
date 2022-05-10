# https://leetcode-cn.com/problems/search-insert-position/

from typing import List


class Solution1:
    '''
    Date: 2022.05.10
    Pass/Error/Bug: 1/3/0
    执行用时：  40 ms, 在所有 Python3 提交中击败了 44.49% 的用户
    内存消耗：15.5 MB, 在所有 Python3 提交中击败了 83.43% 的用户
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:

        length = len(nums)
        if length <= 3:
            if target in nums:
                return nums.index(target)
            else:
                for idx in range(len(nums)):
                    if target < nums[idx]:
                        return idx

                return idx+1

        ls = length // 2

        if nums[ls] > target:
            return self.searchInsert(nums[:ls], target)
        elif nums[ls] < target:
            rs = self.searchInsert(nums[ls:], target)
            return ls + rs
        else:
            rs = []
            for i,v in enumerate(nums):
                if target == v:
                    return i
