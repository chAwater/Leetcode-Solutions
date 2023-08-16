# https://leetcode.cn/problems/number-of-good-pairs/


class Solution1:
    '''
    Date: 2023.08.16
    Pass/Error/Bug: 1/0/0
    执行用时：   48 ms, 在所有 Python3 提交中击败了 42.09% 的用户
    内存消耗：15.71 Mb, 在所有 Python3 提交中击败了 24.78% 的用户
    '''
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_dict = {}
        for n in nums:
            if n in count_dict:
                count_dict[n] += 1
            else:
                count_dict[n] = 1

        n = 0
        for v in count_dict.values():
            if v != 1:
                print (v)
                n += (v)*(v-1)//2

        return n
