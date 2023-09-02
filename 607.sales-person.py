# https://leetcode.cn/problems/sales-person

import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.10
    Pass/Error/Bug: 1/0/0
    执行用时：  528 ms, 在所有 Python3 提交中击败了 12.58% 的用户
    内存消耗：61.80 Mb, 在所有 Python3 提交中击败了  5.60% 的用户
    '''
    names = []

    for g, gdf in pd.merge(
        sales_person,
        pd.merge(orders, company, on='com_id', how='outer'),
        on='sales_id', how='left'
    ).groupby('name_x'):
        if 'RED' in gdf['name_y'].values:
            pass
        else:
            names.append(g)

    return pd.DataFrame({'name': names})
