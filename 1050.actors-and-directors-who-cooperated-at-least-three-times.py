# https://leetcode.cn/problems/actors-and-directors-who-cooperated-at-least-three-times

import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.09
    Pass/Error/Bug: 1/0/0
    执行用时：  284 ms, 在所有 Python3 提交中击败了 46.23% 的用户
    内存消耗：60.60 Mb, 在所有 Python3 提交中击败了 15.63% 的用户
    '''
    return (
        actor_director
        .groupby(['actor_id', 'director_id']).count()
        .query('timestamp>=3')
        .reset_index()
        .drop('timestamp', axis=1)
    )
