# https://leetcode.cn/problems/find-users-with-valid-e-mails

import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.01
    Pass/Error/Bug: 2/3/0
    执行用时：  268 ms, 在所有 Python3 提交中击败了 80.83% 的用户
    内存消耗：60.20 MB, 在所有 Python3 提交中击败了 39.35% 的用户
    '''
    return users[users['mail'].str.match(r'^[a-zA-Z]+[a-zA-Z0-9]*[\._-]*[a-zA-Z0-9]*@leetcode\.com')]
