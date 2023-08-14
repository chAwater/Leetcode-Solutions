# https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer


class Solution1:
    '''
    Date: 2023.08.09
    Pass/Error/Bug: 1/0/0
    执行用时：   44 ms, 在所有 Python3 提交中击败了 42.12% 的用户
    内存消耗：15.48 MB, 在所有 Python3 提交中击败了 59.54% 的用户
    '''
    def subtractProductAndSum(self, n: int) -> int:
        n_prod = 1
        n_sum = 0
        for i in str(n):
            i = int(i)
            n_prod *= i
            n_sum += i

        return n_prod - n_sum
