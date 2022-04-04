# https://leetcode-cn.com/problems/zigzag-conversion/


class Solution1:
    '''
    Date: 2022.04.04
    Pass/Error/Bug: 1/0/1
    执行用时：  60 ms, 在所有 Python3 提交中击败了 56.50% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 92.64% 的用户
    '''
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        o = ''
        total = (numRows-1)*2
        for n in range(numRows):
            idx = 0
            flag = 0

            if (n == 0) or (n == numRows-1):
                step = [total, total]
            else:
                step = [total-2*n, 2*n]

            while n+idx < len(s):
                o += s[n+idx]
                idx += step[flag]
                flag = 0 if flag else 1

        return o
