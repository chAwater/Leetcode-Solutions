# https://leetcode.cn/problems/department-highest-salary

import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.02
    Pass/Error/Bug: 1/0/2
    执行用时：  396 ms, 在所有 Python3 提交中击败了 12.88% 的用户
    内存消耗：61.70 Mb, 在所有 Python3 提交中击败了 12.12% 的用户
    '''
    mdf = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left')
    rdfs = []
    for g, gdf in mdf.groupby('name_y'):
        max_pay = gdf['salary'].max()
        rdfs.append(gdf.query('salary==@max_pay')[['name_y','name_x', 'salary']])

    if len(rdfs) != 0:
        return pd.concat(rdfs).rename(columns={'name_y':'Department', 'name_x':'Employee', 'salary':'Salary'})
    else:
        return pd.DataFrame(columns=['Department', 'Employee', 'Salary'])
