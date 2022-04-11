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
        # Total distance for one zigzag
        total = (numRows - 1) * 2

        for n in range(numRows):
            idx = 0  # Row index
            flag = 0  # Step flag, one big step one small step

            # The first row or the last row
            if (n == 0) or (n == numRows - 1):
                # Zigzag N
                # Total distance means the distance between left | and right |
                step = [total, total]
            else:
                # One big step one small step
                # eg. the first row of |\|, |\ is small step, \| is the big step
                step = [total - 2 * n, 2 * n]

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

        # Output initialization
        # Each row as string
        o_lists = [''] * numRows
        idx = 0  # Row index
        flag = 0  # Flag for two direction

        for sub_s in s:
            o_lists[idx] += sub_s
            if flag == 0:
                # Reach the end, change direction
                if idx == numRows - 1:
                    idx -= 1
                    flag = 1
                # Go down
                else:
                    idx += 1
            elif flag == 1:
                # Reach the end, change direction
                if idx == 0:
                    idx += 1
                    flag = 0
                # Go up
                else:
                    idx -= 1
            else:
                raise

        o = ''
        for ls in o_lists:
            o += ''.join(ls)

        return o
