# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

class Solution1:
    '''
    Date: 2022.04.01
    Pass/Error/Bug: 2/1/0
    执行用时： 444 ms, 在所有 Python3 提交中击败了 10.46% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 98.56% 的用户
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_l = 0
        i_start = 0
        i_end = 1
        max_l = len(s)

        while True:
            if i_end > max_l:
                return max_sub_l
            sub_s = s[i_start:i_end]
            sub_l = i_end - i_start
            if len(dict(zip(sub_s, [1]*sub_l))) == sub_l:
                if max_sub_l < sub_l:
                    max_sub_l = sub_l
                i_end += 1
            else:
                i_start += 1
