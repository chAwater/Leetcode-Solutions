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
