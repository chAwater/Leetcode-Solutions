# https://leetcode.cn/problems/replace-employee-id-with-the-unique-identifier/

import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.09
    Pass/Error/Bug: 1/1/0
    执行用时：  380 ms, 在所有 Python3 提交中击败了 20.60% 的用户
    内存消耗：60.80 MB, 在所有 Python3 提交中击败了 23.77% 的用户
    '''
    return pd.merge(employee_uni, employees, on='id', how='outer').drop('id', axis=1)
