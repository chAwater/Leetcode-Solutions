# https://leetcode-cn.com/problems/valid-sudoku/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [{},{},{},{},{},{},{},{},{}]
        pads = [{},{},{},{},{},{},{},{},{}]
        for rid, row in enumerate(board):
            for cid, v in enumerate(row):
                if v in cols[cid]:
                    return False
                else:
                    if v == '.':
                        continue
                    cols[cid][v] = 1
                pid = 3 * (rid // 3) + (cid // 3)
                if v in pads[pid]:
                    return False
                else:
                    if v == '.':
                        continue
                    pads[pid][v] = 1

        return True
