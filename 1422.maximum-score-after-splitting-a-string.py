# https://leetcode.cn/problems/maximum-score-after-splitting-a-string


class Solution1:
    '''
    Date: 2023.08.21
    Pass/Error/Bug: 1/1/0
    执行用时：   40 ms, 在所有 Python3 提交中击败了 94.18% 的用户
    内存消耗：15.57 Mb, 在所有 Python3 提交中击败了 77.16% 的用户
    '''
    def maxScore(self, s: str) -> int:
        n_zeros = 0
        n_ones = 0
        for n in s:
            if n == '0':
                n_zeros += 1
            else:
                n_ones += 1

        max_score = 0
        left_zeros, left_ones = 0, 0
        right_zeros, right_ones = n_zeros, n_ones

        for n in s[:-1]:
            if n == '0':
                left_zeros += 1
                right_zeros -= 1
            else:
                left_ones += 1
                right_ones -= 1
            score = left_zeros + right_ones
            if score > max_score:
                max_score = score

        return max_score
