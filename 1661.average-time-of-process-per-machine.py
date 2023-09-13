# https://leetcode.cn/problems/average-time-of-process-per-machine

import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.16
    Pass/Error/Bug: 1/0/0
    执行用时：  388 ms, 在所有 Python3 提交中击败了 15.19% 的用户
    内存消耗：58.51 Mb, 在所有 Python3 提交中击败了 84.81% 的用户
    '''
    return (
        activity
        .pivot(index=['machine_id', 'process_id'], columns='activity_type', values='timestamp')
        .reset_index()
        .groupby('machine_id')
        .agg({'process_id':'count', 'start':'sum', 'end':'sum'})
        .apply(lambda row: round((row['end']-row['start'])/row['process_id'], 3), axis=1)
        .reset_index()
        .rename(columns={0:'processing_time'})
    )
