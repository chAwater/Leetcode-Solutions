# https://leetcode.cn/problems/rank-scores

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.27
    Pass/Error/Bug: 1/0/0
    执行用时：  321 ms, 在所有 Python3 提交中击败了 15.20% 的用户
    内存消耗：61.40 Mb, 在所有 Python3 提交中击败了  5.63% 的用户
    '''
    u_score = scores.sort_values('score', ascending=False)['score'].unique()
    rank_df = pd.DataFrame(u_score, columns=['score'], index=range(1, u_score.shape[0]+1)).reset_index()
    return pd.merge(
        scores, rank_df, on='score', how='left'
    ).sort_values('score', ascending=False)[['score', 'index']].rename(columns={'index':'rank'})
