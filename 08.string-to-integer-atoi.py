# https://leetcode-cn.com/problems/string-to-integer-atoi/

import re


class Solution1:
    '''
    Date: 2022.04.06
    Pass/Error/Bug: 1/3/1
    执行用时：  48 ms, 在所有 Python3 提交中击败了 19.83% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 39.27% 的用户
    '''
    def myAtoi(self, s: str) -> int:
        mtag = 0  # flag for plus or minus
        ntag = 0  # flag for number start
        ns = '0'  # output

        for sub_s in s:
            if ntag * mtag == 0:
                if sub_s == ' ':
                    continue
                elif sub_s == '+':
                    ntag = 1
                    mtag = 1
                    continue
                elif sub_s == '-':
                    mtag = -1
                    ntag = 1
                    continue

            if sub_s in '0123456789.':
                mtag = 1 if mtag != -1 else -1
                ntag = 1
                ns += sub_s
            else:
                break

        ns = mtag * int(float(ns))
        if ns > 2**31-1:
            return 2**31-1
        if ns < -2**31:
            return -2**31
        return ns


class Solution2:
    '''
    Date: 2022.04.06
    Pass/Error/Bug: 1/2/1
    执行用时：  44 ms, 在所有 Python3 提交中击败了 41.37% 的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了 94.41% 的用户
    '''
    def myAtoi(self, s: str) -> int:
        ns = re.findall(r'^[\+\-]?\d+', s.lstrip(' '))
        if ns:
            return max(min(int(ns[0]), 2**31-1), -2**31)
        else:
            return 0
