# https://leetcode.cn/problems/product-sales-analysis-i

import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.09.03
    Pass/Error/Bug: 1/0/0
    执行用时：  332 ms, 在所有 Python3 提交中击败了 62.71% 的用户
    内存消耗：61.35 Mb, 在所有 Python3 提交中击败了  6.78% 的用户
    '''
    return pd.merge(sales, product, on='product_id').groupby(['product_name', 'year', 'price']).size().reset_index().drop(0, axis=1)
