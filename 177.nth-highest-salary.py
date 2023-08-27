# https://leetcode.cn/problems/nth-highest-salary

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    '''
    Date: 2023.08.02
    Pass/Error/Bug: 1/0/0
    执行用时：  300 ms, 在所有 Python3 提交中击败了 18.59% 的用户
    内存消耗：60.60 Mb, 在所有 Python3 提交中击败了  5.50% 的用户
    '''
    gdf = employee.groupby('salary').first().sort_index(ascending=False).reset_index()
    if gdf.shape[0] < N:
        return pd.DataFrame([None], index=[0], columns=['getNthHighestSalary({})'.format(N)])
    else:
        return pd.DataFrame([gdf.loc[N-1,'salary']], index=[0], columns=['getNthHighestSalary({})'.format(N)])
