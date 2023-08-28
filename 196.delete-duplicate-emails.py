# https://leetcode.cn/problems/delete-duplicate-emails

import pandas as pd


# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    '''
    Date: 2023.08.03
    Pass/Error/Bug: 1/0/0
    执行用时：  244 ms, 在所有 Python3 提交中击败了 93.68% 的用户
    内存消耗：60.40 Mb, 在所有 Python3 提交中击败了 37.94% 的用户
    '''
    kept_idx = person.groupby('email')['id'].transform('min')
    drop_idx = person[person['id']!=kept_idx].index
    person.drop(drop_idx, inplace=True)
    return
