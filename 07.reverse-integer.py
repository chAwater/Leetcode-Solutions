# https://leetcode-cn.com/problems/reverse-integer/

class Solution1:
    '''
    Date: 2022.04.05
    Pass/Error/Bug: 1/3/0
    执行用时：  36 ms, 在所有 Python3 提交中击败了 76.48% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 77.08% 的用户
    '''
    def reverse(self, x: int) -> int:
        tag = 1 if x > 0 else -1
        o = tag * int(str(tag * x)[::-1])
        if -2**31 <= o <= 2**31-1:
            return o
        else:
            return 0
