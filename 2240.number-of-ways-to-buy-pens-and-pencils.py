# https://leetcode.cn/problems/number-of-ways-to-buy-pens-and-pencils


class Solution1:
    '''
    Date: 2023.09.01
    Pass/Error/Bug: 1/2/0
    执行用时：  380 ms, 在所有 Python3 提交中击败了 78.99% 的用户
    内存消耗：15.72 MB, 在所有 Python3 提交中击败了 34.06% 的用户
    '''
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        cost_min = min(cost1, cost2)
        cost_max = max(cost1, cost2)

        n_res = 0
        for i in range(total // cost_max + 1):
            n_res += (total - i * cost_max) // cost_min + 1

        return n_res
