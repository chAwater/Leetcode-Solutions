# https://leetcode.cn/problems/managers-with-at-least-5-direct-reports

import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.10
    Pass/Error/Bug: 2/5/0
    执行用时：  276 ms, 在所有 Python3 提交中击败了 52.12% 的用户
    内存消耗：62.00 Mb, 在所有 Python3 提交中击败了  5.13% 的用户
    '''
    return (
        pd.merge(employee, employee, left_on='managerId', right_on='id', how='left')
        .reset_index()
        .groupby(['id_y', 'name_y']).count()
        .query('name_x>=5')
        .reset_index()
        .rename(columns={'name_y':'name'})[['name']]
    )
