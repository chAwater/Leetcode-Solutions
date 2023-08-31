# https://leetcode.cn/problems/customer-placing-the-largest-number-of-orders

import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.07
    Pass/Error/Bug: 1/0/0
    执行用时：  280 ms, 在所有 Python3 提交中击败了 66.40% 的用户
    内存消耗：60.20 Mb, 在所有 Python3 提交中击败了 41.33% 的用户
    '''
    return (
        orders
        .groupby('customer_number').count()
        .sort_values('order_number', ascending=False)
        .reset_index().head(1)[['customer_number']]
    )
