# https://leetcode.cn/problems/user-activity-for-the-past-30-days-i

import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.09.09
    Pass/Error/Bug: 1/1/0
    执行用时：  408 ms, 在所有 Python3 提交中击败了 22.45% 的用户
    内存消耗：60.27 Mb, 在所有 Python3 提交中击败了  6.12% 的用户
    '''
    tdf = (
        activity
        .groupby(['activity_date', 'user_id']).first()
        .reset_index()
        .groupby('activity_date')['user_id'].count()
        .reset_index()
        .rename(columns={'activity_date':'day', 'user_id':'active_users'})
    )

    return tdf[(tdf['day']>'2019-06-27') & (tdf['day']<='2019-07-27')]
