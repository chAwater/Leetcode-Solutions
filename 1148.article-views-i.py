# https://leetcode.cn/problems/article-views-i

import pandas as pd


def article_views_i(views: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.01
    Pass/Error/Bug: 1/0/0
    执行用时：  276 ms, 在所有 Python3 提交中击败了 75.42% 的用户
    内存消耗：60.80 Mb, 在所有 Python3 提交中击败了 30.18% 的用户
    '''
    return (
        views.query('viewer_id == author_id')[['author_id']]
        .rename(columns={'author_id':'id'})
        .drop_duplicates()
        .sort_values('id')
    )
