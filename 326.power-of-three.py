# https://leetcode.cn/problems/power-of-three


class Solution1:
    '''
    Date: 2023.08.17
    Pass/Error/Bug: 1/0/0
    执行用时：   76 ms, 在所有 Python3 提交中击败了 86.69% 的用户
    内存消耗：15.73 Mb, 在所有 Python3 提交中击败了 30.27% 的用户
    '''
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        elif n % 3 == 0:
            return self.isPowerOfThree(n//3)
        else:
            return False
