# https://leetcode.cn/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidnates: List[int], target: int) -> List[List[int]]:
        merged_rs = []

        for idx, num in enumerate(candidnates):
            new_target = target - num
            if new_target < 0:
                continue
            elif new_target > 0:
                rs = self.combinationSum(candidnates[idx:], new_target)
                if rs == []:
                    continue
                else:
                    for r in rs:
                        merged_rs.append([num] + r)
            else:
                merged_rs.append([num])

        return merged_rs
