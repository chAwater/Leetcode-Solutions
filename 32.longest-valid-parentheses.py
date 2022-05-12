# https://leetcode.cn/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        rs = 0
        ls = len(s)
        for idx_s in range(ls):
            if s[idx_s] != '(':
                continue

            cache = 0
            trs = 0

            for step in range(0,ls-idx_s):
                if cache < 0:
                    step -= 1
                    break

                if s[idx_s+step] == '(':
                    cache += 1
                else:
                    cache -= 1
                    trs += 2

            if cache > 0:
                trs -= 2

            if trs > rs:
                rs = trs

        return rs
