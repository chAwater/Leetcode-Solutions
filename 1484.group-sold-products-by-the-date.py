# https://leetcode.cn/problems/group-sold-products-by-the-date

import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.08
    Pass/Error/Bug: 1/1/0
    执行用时：  328 ms, 在所有 Python3 提交中击败了 58/85% 的用户
    内存消耗：61.20 MB, 在所有 Python3 提交中击败了 63.68% 的用户
    '''
    return (
        activities
        .groupby('sell_date').agg(
            num_sold=('product', 'nunique'),
            products=('product', lambda x:','.join(sorted(set(x))))
        )
        .reset_index()
        .sort_values('sell_date', ascending=True)
    )
