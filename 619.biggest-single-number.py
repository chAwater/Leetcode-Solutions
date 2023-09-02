# https://leetcode.cn/problems/biggest-single-number

import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.31
    Pass/Error/Bug: 1/0/0
    执行用时：  280 ms, 在所有 Python3 提交中击败了 53.34% 的用户
    内存消耗：59.30 Mb, 在所有 Python3 提交中击败了 61.97% 的用户
    '''
    rdf = (
        my_numbers
        .groupby('num').size()
        .reset_index()
        .rename(columns={0:'count'})
        .query('count==1')
        .sort_values('num', ascending=False)
        .head(1)
        .drop('count', axis=1)
    )
    if rdf.shape[0] == 0:
        return pd.DataFrame([None], columns=['num'])
    else:
        return rdf
