# https://leetcode.cn/problems/transpose-matrix


class Solution:
    '''
    Date: 2023.08.20
    Pass/Error/Bug: 1/0/0
    执行用时：   48 ms, 在所有 Python3 提交中击败了 51.33% 的用户
    内存消耗：16.35 Mb, 在所有 Python3 提交中击败了 47.72% 的用户
    '''
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        new_matrix = []
        for c in range(n_cols):
            new_rows = []
            for r in range(n_rows):
                new_rows.append(matrix[r][c])

            new_matrix.append(new_rows)

        return new_matrix
