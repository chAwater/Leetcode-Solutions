# https://leetcode.cn/problems/second-highest-salary

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.02
    Pass/Error/Bug: 1/0/0
    执行用时：  252 ms, 在所有 Python3 提交中击败了 47.88% 的用户
    内存消耗：60.40 Mb, 在所有 Python3 提交中击败了  7.78% 的用户
    '''
    gdf = employee.groupby('salary').first().sort_index(ascending=False).reset_index()
    if gdf.shape[0] < 2:
        return pd.DataFrame([None], index=[0], columns=['SecondHighestSalary'])
    else:
        return pd.DataFrame([gdf.loc[1,'salary']], index=[0], columns=['SecondHighestSalary'])
