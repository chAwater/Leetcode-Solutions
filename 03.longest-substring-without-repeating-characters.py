# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

class Solution1:
    '''
    Date: 2022.04.01
    Pass/Error/Bug: 1/0/0
    执行用时： 568 ms, 在所有 Python3 提交中击败了  8.06% 的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了 29.34% 的用户
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_l = 0
        for idx in range(len(s)):
            sub_s = s[idx]
            sub_i = 0
            while True:
                sub_next = s[idx+sub_i+1:idx+sub_i+2]
                if sub_next in sub_s:
                    break
                else:
                    sub_s += sub_next
                    sub_i += 1

            if max_sub_l <= len(sub_s):
                max_sub_l = len(sub_s)

        return max_sub_l
