# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

from typing import List, Union


class Solution1:
    '''
    Date: 2022.04.16
    Pass/Error/Bug: 1/1/0
    执行用时：  36 ms, 在所有 Python3 提交中击败了 65.93% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 96.96% 的用户
    '''
    def add_helper(self, ds: str, slist: List[str]) -> Union[str, List]:
        if len(slist) == 0:
            return ds
        else:
            return [ ds+s for s in slist ]

    def letterCombinations(self, digits: str) -> List[str]:
        nine_dict = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }

        if digits == '':
            return []
        else:
            rs = []
            for ds in nine_dict[digits[0]]:
                rs += self.add_helper(ds, self.letterCombinations(digits[1:]))
            return rs
