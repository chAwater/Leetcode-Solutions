# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution1:
    '''
    Date: 2022.05.06
    Pass/Error/Bug: 1/0/0
    执行用时：  40 ms, 在所有 Python3 提交中击败了 45.86% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了 89.88% 的用户
    '''
    def search(self, nums: List[int], target: int) -> int:
        idx = 0
        while idx < len(nums):
            if target == nums[idx]:
                return idx

            idx += 1

        return -1


class Solution2:
    '''
    Date: 2022.05.06
    Pass/Error/Bug: 1/1/1
    执行用时：  40 ms, 在所有 Python3 提交中击败了 45.86% 的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了 44.31% 的用户
    '''
    def search(self, nums: List[int], target: int) -> int:
        flag = 0
        idx = 0
        while idx < len(nums):
            if (idx > 1) and (nums[idx] < nums[idx-1]) and (target < nums[idx]):
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


class Solution3:
    '''
    Date: 2022.05.06
    Pass/Error/Bug: 1/0/0
    执行用时：  48 ms, 在所有 Python3 提交中击败了  6.93% 的用户
    内存消耗：15.3 MB, 在所有 Python3 提交中击败了 22.71% 的用户
    '''
    def search(self, nums: List[int], target: int) -> int:
        ls = len(nums)

        if ls == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        a = self.search(nums[:ls // 2], target)
        b = self.search(nums[ls // 2:], target)

        if (a != -1):
            if (b == -1):
                return a
            else:
                return -1
        else:
            if (b != -1):
                return ls // 2 + b
            else:
                return -1


class Solution4:
    '''
    Date: 2022.05.06
    Pass/Error/Bug: 1/0/0
    执行用时：  40 ms, 在所有 Python3 提交中击败了 45.81% 的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了 56.71% 的用户
    '''
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
