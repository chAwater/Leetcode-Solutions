# https://leetcode.cn/problems/customers-who-bought-all-products

import pandas as pd


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.09.06
    Pass/Error/Bug: 1/1/0
    执行用时：  264 ms, 在所有 Python3 提交中击败了 82.14% 的用户
    内存消耗：59.22 Mb, 在所有 Python3 提交中击败了 25.00% 的用户
    '''
    n_product = product.shape[0]
    return (
        customer
        .groupby(['customer_id', 'product_key']).nunique()
        .reset_index()
        .groupby(['customer_id'])['product_key'].count()
        .reset_index()
        .query('product_key==@n_product')
        .drop('product_key', axis=1)
    )
