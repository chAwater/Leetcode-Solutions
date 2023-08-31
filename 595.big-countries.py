# https://leetcode.cn/problems/big-countries

import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.07.31
    Pass/Error/Bug: 1/1/0
    执行用时：  292 ms, 在所有 Python3 提交中击败了 21.90% 的用户
    内存消耗：61.30 Mb, 在所有 Python3 提交中击败了 79.58% 的用户
    '''
    return world.query('area >= 3000000 or population >= 25000000')[['name','population','area']]
