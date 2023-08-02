# https://leetcode.cn/problems/plus-one

from typing import List


class Solution1:
    '''
    Date: 2023.08.02
    Pass/Error/Bug: 1/0/0
    执行用时：   52 ms, 在所有 Python3 提交中击败了  9.33% 的用户
    内存消耗：15.63 MB, 在所有 Python3 提交中击败了 40.02% 的用户
    '''
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int(''.join([str(i) for i in digits]))+1
        return [int(i) for i in str(s)]


class Solution2:
    '''
    Date: 2023.08.02
    Pass/Error/Bug: 1/1/0
    执行用时：   40 ms, 在所有 Python3 提交中击败了 65.07% 的用户
    内存消耗：15.69 MB, 在所有 Python3 提交中击败了 24.95% 的用户
    '''
    def plusOne(self, digits: List[int]) -> List[int]:
        e_idx = len(digits)
        for idx in range(e_idx-1, -1, -1):
            if digits[idx] != 9:
                digits[idx] += 1
                return digits
            else:
                digits[idx] = 0

        return [1] + digits
