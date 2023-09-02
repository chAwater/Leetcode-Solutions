# https://leetcode.cn/problems/sales-analysis-iii

import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.09.03
    Pass/Error/Bug: 1/2/0
    执行用时：  344 ms, 在所有 Python3 提交中击败了 67.57% 的用户
    内存消耗：62.78 Mb, 在所有 Python3 提交中击败了  5.41% 的用户
    '''
    mdf = pd.merge(sales, product, on='product_id')
    remove_df = mdf[(mdf['sale_date']>'2019-03-31') | (mdf['sale_date']<'2019-01-01')]
    return (
        mdf.set_index('product_id')
        .drop(remove_df['product_id'])
        .reset_index()[['product_id','product_name']]
        .drop_duplicates()
    )
