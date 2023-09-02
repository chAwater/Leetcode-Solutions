# https://leetcode.cn/problems/swap-salary

import pandas as pd


def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.09.02
    Pass/Error/Bug: 1/0/0
    执行用时：  236 ms, 在所有 Python3 提交中击败了 80.85% 的用户
    内存消耗：57.19 Mb, 在所有 Python3 提交中击败了 93.62% 的用户
    '''
    return salary.replace({'sex':{'f':'m', 'm':'f'}})
