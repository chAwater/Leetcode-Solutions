# https://leetcode-cn.com/problems/longest-common-prefix/

from typing import List


class Solution1:
    '''
    Date: 2022.04.14
    Pass/Error/Bug: 1/0/0
    执行用时：  36 ms, 在所有 Python3 提交中击败了 75.47% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 96.39% 的用户
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = ''
        for i in list(map(set, zip(*strs))):
            if len(i) == 1:
                r += list(i)[0]
            else:
                break
        return r


class Solution2:
    '''
    Date: 2022.04.14
    Pass/Error/Bug: 1/0/0
    执行用时：  40 ms, 在所有 Python3 提交中击败了 51.41% 的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了 22.28% 的用户
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        a, b = strs[0], strs[-1]
        r = ''
        for idx, sub_s in enumerate(a):
            if sub_s == b[idx]:
                r += sub_s
            else:
                break
        return r


class Solution3:
    '''
    Date: 2022.04.15
    Pass/Error/Bug: 1/0/0
    执行用时：  40 ms, 在所有 Python3 提交中击败了 51.66% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了 24.77% 的用户
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        a, b = min(strs), max(strs)
        r = ''
        for t in list(zip(a, b)):
            if t[0] == t[1]:
                r += t[0]
            else:
                break
        return r
