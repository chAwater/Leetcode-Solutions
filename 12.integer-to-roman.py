# https://leetcode-cn.com/problems/integer-to-roman/


class Solution1:
    '''
    Date: 2022.04.12
    Pass/Error/Bug: 1/1/0
    执行用时：  44 ms, 在所有 Python3 提交中击败了 84.46% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了  9.22% 的用户
    '''
    def intToRoman(self, num: int) -> str:
        roman_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        n_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        s = ''
        for idx in range(13):
            while num >= n_list[idx]:
                s += roman_list[idx]
                num -= n_list[idx]

        return s
