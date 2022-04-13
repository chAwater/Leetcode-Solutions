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


class Solution2:
    '''
    Date: 2022.04.13
    Pass/Error/Bug: 1/0/0
    执行用时：  48 ms, 在所有 Python3 提交中击败了 74.47% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 51.09% 的用户
    '''
    def romanToInt(self, s: str) -> int:
        s = s.replace('IV', '|4|')
        s = s.replace('IX', '|9|')
        s = s.replace('XL', '|40|')
        s = s.replace('XC', '|90|')
        s = s.replace('CD', '|400|')
        s = s.replace('CM', '|900|')
        s = s.replace('I', '|1|')
        s = s.replace('V', '|5|')
        s = s.replace('X', '|10|')
        s = s.replace('L', '|50|')
        s = s.replace('C', '|100|')
        s = s.replace('D', '|500|')
        s = s.replace('M', '|1000|')

        r = 0
        for i in s.split('|'):
            if i != '':
                r += int(i)

        return r

        # Slower
        # r = [ int(i) for i in s.split('|') if i!='' ]
        # return sum(r)
