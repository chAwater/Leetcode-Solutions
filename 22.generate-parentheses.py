# https://leetcode-cn.com/problems/generate-parentheses/

from typing import List


class Solution1:
    '''
    Date: 2022.04.24
    Pass/Error/Bug: 1/2/0
    执行用时：  44 ms, 在所有 Python3 提交中击败了 31.89% 的用户
    内存消耗：15.3 MB, 在所有 Python3 提交中击败了 19.21% 的用户
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        else:
            rs = {}

            for s in self.generateParenthesis(n-1):
                rs[s + '()'] = 1
                rs['()' + s] = 1
                rs['(' + s + ')'] = 1
                for idx in range(len(s)):
                    rs[s[:idx] + '()' + s[idx:]] = 1

            return list(rs.keys())
