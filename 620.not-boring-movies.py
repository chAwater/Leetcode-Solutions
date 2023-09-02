# https://leetcode.cn/problems/not-boring-movies

import pandas as pd


def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.09.01
    Pass/Error/Bug: 1/0/0
    执行用时：  256 ms, 在所有 Python3 提交中击败了 60.00% 的用户
    内存消耗：60.20 Mb, 在所有 Python3 提交中击败了  5.45% 的用户
    '''
    return cinema.query('description != "boring" and id % 2 == 1').sort_values('rating', ascending=False)
