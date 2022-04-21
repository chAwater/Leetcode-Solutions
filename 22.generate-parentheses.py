# https://leetcode-cn.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        else:
            rs = {}

            for s in self.generateParenthesis(n-1):
                rs[s + '()'] = 1
                rs['()' + s] = 1
                rs['(' + s + ')'] = 1

            return list(rs.keys())



