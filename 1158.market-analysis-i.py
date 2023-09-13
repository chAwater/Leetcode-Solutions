# https://leetcode.cn/problems/market-analysis-i

import pandas as pd


def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.10
    Pass/Error/Bug: 1/0/0
    执行用时：  372 ms, 在所有 Python3 提交中击败了 79.03% 的用户
    内存消耗：60.26 Mb, 在所有 Python3 提交中击败了 32.26% 的用户
    '''
    return (
        pd.merge(
            users,
            orders[orders['order_date'].astype(str).str.contains('2019')],
            left_on='user_id', right_on='buyer_id',
            how='left'
        )
        .groupby('user_id')
        .agg({'join_date':'first','order_id':'count'})
        .reset_index()
        .rename(columns={'user_id':'buyer_id','order_id':'orders_in_2019'})
    )
