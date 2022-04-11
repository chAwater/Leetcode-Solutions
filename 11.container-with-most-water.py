# https://leetcode-cn.com/problems/container-with-most-water/

from typing import List


class Solution1:
    '''
    Date: 2022.04.11
    Pass/Error/Bug: 1/2/0
    执行用时： 184 ms, 在所有 Python3 提交中击败了 71.48% 的用户
    内存消耗：24.2 MB, 在所有 Python3 提交中击败了 79.28% 的用户
    '''
    def maxArea(self, height: List[int]) -> int:

        x1 = 0
        x2 = len(height) - 1
        amax = (x2 - x1) * min(height[x1], height[x2])

        while x1 != x2:
            a = (x2 - x1) * min(height[x1], height[x2])
            if a > amax:
                amax = a

            # Move the shorter one, to increase the height
            if height[x1] > height[x2]:
                x2 -= 1
            else:
                x1 += 1

        return amax
