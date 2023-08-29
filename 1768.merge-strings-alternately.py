# https://leetcode-cn.com/problems/merge-strings-alternately

from typing import List


class Solution1:
    '''
    Date: 2022.08.29
    Pass/Error/Bug: 1/0/0
    执行用时：   44 ms, 在所有 Python3 提交中击败了 59.14% 的用户
    内存消耗：15.74 MB, 在所有 Python3 提交中击败了 19.21% 的用户
    '''
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1 = 0
        idx2 = 0
        result = ''
        length1 = len(word1)
        length2 = len(word2)

        if length1 <= length2:
            while idx1 < length1:
                result += word1[idx1]
                result += word2[idx2]
                idx1 += 1
                idx2 += 1
            result += word2[idx2:]
        else:
            while idx2 < length2:
                result += word1[idx1]
                result += word2[idx2]
                idx1 += 1
                idx2 += 1
            result += word1[idx2:]

        return result
