# https://leetcode.cn/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        merged_rs = []
        for idx, num in enumerate(candidates):

            new_target = target - num
            if new_target < 0:
                continue
            elif new_target > 0:
                rs = self.combinationSum2(candidates[idx+1:], new_target)
                if rs == []:
                    continue
                else:
                    for r in rs:
                        merged_rs.append( [num] + r )
            else:
                merged_rs.append( [num] )

        return merged_rs
