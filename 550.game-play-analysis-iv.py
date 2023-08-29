# https://leetcode.cn/problems/game-play-analysis-iv

import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.30
    Pass/Error/Bug: 1/0/0
    执行用时： 1172 ms, 在所有 Python3 提交中击败了  5.71% 的用户
    内存消耗：59.93 Mb, 在所有 Python3 提交中击败了 71.43% 的用户
    '''
    return (
        pd.merge(employee, employee, left_on='managerId', right_on='id', how='left')
        .reset_index()
        .groupby(['id_y', 'name_y']).count()
        .query('name_x>=5')
        .reset_index()
        .rename(columns={'name_y':'name'})[['name']]
    )
    n = 0
    for g, gdf in activity.groupby('player_id'):
        tdf = gdf.sort_values('event_date').diff()

        if (tdf.shape[0] >= 2) and (tdf.iloc[1, 2] == pd.Timedelta(days=1)):
            n += 1

    total = activity['player_id'].unique().shape[0]
    return pd.DataFrame({'fraction' : round(n/total, 2)}, index=[0])
