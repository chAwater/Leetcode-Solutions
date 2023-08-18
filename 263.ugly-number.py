# https://leetcode.cn/problems/ugly-number


class Solution1:
    '''
    Date: 2023.08.18
    Pass/Error/Bug: 1/0/1
    执行用时：   40 ms, 在所有 Python3 提交中击败了 84.57% 的用户
    内存消耗：15.70 Mb, 在所有 Python3 提交中击败了 26.07% 的用户
    '''
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        elif n % 2 == 0:
            return self.isUgly(n//2)
        elif n % 3 == 0:
            return self.isUgly(n//3)
        elif n % 5 == 0:
            return self.isUgly(n//5)
        else:
            return False
