# https://leetcode.cn/problems/power-of-two


class Solution1:
    '''
    Date: 2023.08.17
    Pass/Error/Bug: 1/0/2
    执行用时：   40 ms, 在所有 Python3 提交中击败了 86.38% 的用户
    内存消耗：15.50 Mb, 在所有 Python3 提交中击败了 87.64% 的用户
    '''
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        elif n % 2 == 0:
            return self.isPowerOfTwo(n//2)
        else:
            return False
