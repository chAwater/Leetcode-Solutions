# https://leetcode.cn/problems/combine-two-tables

import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.23
    Pass/Error/Bug: 1/0/0
    执行用时：  264 ms, 在所有 Python3 提交中击败了 70.44% 的用户
    内存消耗：60.60 Mb, 在所有 Python3 提交中击败了 48.43% 的用户
    '''
    return pd.merge(person, address, on='personId', how='left').drop(['personId', 'addressId'], axis=1)
