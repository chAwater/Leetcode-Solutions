# https://leetcode.cn/problems/reverse-string/


class Solution:
    '''
    Date: 2023.08.07
    Pass/Error/Bug: 1/0/0
    执行用时：   48 ms, 在所有 Python3 提交中击败了 60.86% 的用户
    内存消耗：20.96 Mb, 在所有 Python3 提交中击败了 21.09% 的用户
    '''
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
