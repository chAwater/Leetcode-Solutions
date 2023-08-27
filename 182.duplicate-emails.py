# https://leetcode.cn/problems/duplicate-emails

import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.28
    Pass/Error/Bug: 1/0/0
    执行用时：  252 ms, 在所有 Python3 提交中击败了 83.33% 的用户
    内存消耗：58.59 Mb, 在所有 Python3 提交中击败了 35.00% 的用户
    '''
    return (
        person.groupby('email').size()
        .reset_index()
        .rename(columns={0:'count', 'email':'Email'})
        .query('count>1')[['Email']]
    )
