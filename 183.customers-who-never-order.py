# https://leetcode.cn/problems/customers-who-never-order

import pandas as pd


def customers_who_never_order(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.01
    Pass/Error/Bug: 2/0/0
    执行用时：  288 ms, 在所有 Python3 提交中击败了 38.14% 的用户
    内存消耗：60.60 Mb, 在所有 Python3 提交中击败了 12.85% 的用户
    '''
    return (
        pd.merge(
            customers,
            orders,
            left_on='id',
            right_on='customerId',
            how='outer'
        ).query('customerId != 0')
        .fillna(0).query('customerId == 0')[['name']].rename(columns={'name':'Customers'})
    )
