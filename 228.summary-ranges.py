# https://leetcode.cn/problems/summary-ranges


class Solution1:
    '''
    Date: 2023.08.26
    Pass/Error/Bug: 1/0/1
    执行用时：   40 ms, 在所有 Python3 提交中击败了 77.55% 的用户
    内存消耗：15.72 Mb, 在所有 Python3 提交中击败了 30.43% 的用户
    '''
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        result = []
        tmp = nums[0]
        s = '{}'.format(tmp)
        arrow_tag = 0
        for n in nums[1:]:
            if n == tmp + 1:
                if arrow_tag == 0:
                    s += '->'
                    arrow_tag = 1
            else:
                if arrow_tag == 1:
                    arrow_tag = 0
                    s += '{}'.format(tmp)

                result.append(s)
                s = '{}'.format(n)

            tmp = n

        if arrow_tag == 1:
            arrow_tag = 0
            s += '{}'.format(tmp)
        result.append(s)

        return result
