# https://leetcode.cn/problems/employees-earning-more-than-their-managers

import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.27
    Pass/Error/Bug: 1/0/0
    执行用时：  460 ms, 在所有 Python3 提交中击败了 15.58% 的用户
    内存消耗：59.60 Mb, 在所有 Python3 提交中击败了 98.70% 的用户
    '''
    return (
        pd.merge(employee, employee, left_on='managerId', right_on='id', how='left')
        .query('salary_x>salary_y')[['name_x']]
        .rename(columns={'name_x':'Employee'})
    )
