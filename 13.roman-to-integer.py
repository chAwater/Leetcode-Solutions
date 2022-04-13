# https://leetcode-cn.com/problems/roman-to-integer/


class Solution1:
    '''
    Date: 2022.04.13
    Pass/Error/Bug: 1/0/0
    执行用时：  56 ms, 在所有 Python3 提交中击败了 33.46% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 82.74% 的用户
    '''
    def romanToInt(self, s: str) -> int:
        r = 0
        romandict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        for i in range(len(s)):
            sub_s = s[i]
            if (i+1 < len(s)) and (romandict[sub_s] < romandict[s[i+1]]):
                r -= romandict[sub_s]
            else:
                r += romandict[sub_s]

        return r
