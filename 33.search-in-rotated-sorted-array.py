# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except:
        #     return -1

        flag = 0
        idx = 0
        while idx < len(nums):
            if (idx > 1) and (nums[idx] > nums[idx-1]):
                flag = 1

            if target < nums[idx]:
                idx += 1
            elif target == nums[idx]:
                return idx
            else:
                if flag == 0:
                    idx += 1
                else:
                    return -1

        return -1
