# https://leetcode.cn/problems/form-smallest-number-from-two-digit-arrays


class Solution1:
    '''
    Date: 2023.09.05
    Pass/Error/Bug: 1/0/0
    执行用时：   40 ms, 在所有 Python3 提交中击败了 81.18% 的用户
    内存消耗：15.59 Mb, 在所有 Python3 提交中击败了 62.37% 的用户
    '''
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        m1 = min(nums1)
        m2 = min(nums2)

        share = set(nums1) & set(nums2)

        if m1 > m2:
            comb = int(str(m2) + str(m1))
        else:
            comb = int(str(m1) + str(m2))

        if share:
            share = min(share)
        else:
            share = comb

        return min(share, comb)
