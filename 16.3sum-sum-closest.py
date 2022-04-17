# https://leetcode-cn.com/problems/3sum-closest/

from typing import List


class Solution1:
    '''
    Date: 2022.04.15
    Pass/Error/Bug: 1/3/2
    执行用时： 224 ms, 在所有 Python3 提交中击败了 46.56% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了 23.55% 的用户
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ls = len(nums)
        diff = 9999
        rs = sum(nums[:3])

        for idx1 in range(ls):
            idx2 = idx1 + 1
            idx3 = ls - 1

            while idx2 < idx3:
                candidate = [nums[idx1], nums[idx2], nums[idx3]]
                sum3 = sum(candidate)

                if sum3 > target:
                    new_diff = sum3 - target
                    if new_diff < diff:
                        diff = new_diff
                        rs = sum3
                    idx3 -= 1
                elif sum3 < target:
                    new_diff = target - sum3
                    if new_diff < diff:
                        diff = new_diff
                        rs = sum3
                    idx2 += 1
                else:
                    return target

        return rs
