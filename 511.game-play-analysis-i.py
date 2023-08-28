# https://leetcode.cn/problems/game-play-analysis-i

import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.06
    Pass/Error/Bug: 1/0/0
    执行用时：  292 ms, 在所有 Python3 提交中击败了 59.61% 的用户
    内存消耗：61.00 Mb, 在所有 Python3 提交中击败了 79.48% 的用户
    '''
    return activity.groupby('player_id')['event_date'].min().reset_index().rename(columns={'event_date':'first_login'})
