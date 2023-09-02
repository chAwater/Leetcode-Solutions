# https://leetcode.cn/problems/patients-with-a-condition

import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.01
    Pass/Error/Bug: 1/0/0
    执行用时：  332 ms, 在所有 Python3 提交中击败了  9.00% 的用户
    内存消耗：59.70 MB, 在所有 Python3 提交中击败了  5.32% 的用户
    '''
    patients['npos'] = patients['conditions'].apply(lambda x: sum(c.startswith('DIAB1') for c in x.split(' ')))
    return patients.query('npos>0').drop('npos', axis=1)
