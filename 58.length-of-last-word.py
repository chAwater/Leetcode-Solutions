# https://leetcode.cn/problems/length-of-last-word


class Solution1:
    '''
    Date: 2023.08.02
    Pass/Error/Bug: 1/0/0
    执行用时：   44 ms, 在所有 Python3 提交中击败了 42.29% 的用户
    内存消耗：15.64 MB, 在所有 Python3 提交中击败了 49.91% 的用户
    '''
    def lengthOfLastWord(self, s: str) -> int:
        slen = len(s)
        while True:
            s = s.replace('  ', ' ')
            tlen = len(s)
            if slen == tlen:
                break
            else:
                slen = tlen

        slist = s.split(' ')

        if slist[-1] == '':
            return len(slist[-2])
        else:
            return len(slist[-1])
