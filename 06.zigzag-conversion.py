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


class Solution2:
    '''
    Date: 2022.04.04
    Pass/Error/Bug: 1/0/0
    执行用时：  64 ms, 在所有 Python3 提交中击败了 43.49% 的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了 46.50% 的用户
    '''
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            o_lists = [''] * numRows
            idx = 0
            flag = 0
            for sub_s in s:
                o_lists[idx] += sub_s
                if flag == 0:
                    if idx == numRows-1:
                        idx -= 1
                        flag = 1
                    else:
                        idx += 1
                elif flag == 1:
                    if idx == 0:
                        idx += 1
                        flag = 0
                    else:
                        idx -= 1
                else:
                    raise

            o = ''
            for ls in o_lists:
                o += ''.join(ls)

            return o
