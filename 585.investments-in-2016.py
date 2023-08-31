# https://leetcode.cn/problems/investments-in-2016

import pandas as pd


def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.09.01
    Pass/Error/Bug: 1/0/0
    执行用时：  384 ms, 在所有 Python3 提交中击败了 43.24% 的用户
    内存消耗：58.72 Mb, 在所有 Python3 提交中击败了 81.08% 的用户
    '''
    cond1 = insurance['tiv_2015'].duplicated(keep=False)
    cond2 = insurance[['lat', 'lon']].duplicated(keep=False)
    return pd.DataFrame(
        [round(insurance[(cond1 & ~cond2)].loc[:, 'tiv_2016'].sum(), 2)],
        columns=['tiv_2016']
    )

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.09.01
    Pass/Error/Bug: 1/0/0
    执行用时：  464 ms, 在所有 Python3 提交中击败了 32.42% 的用户
    内存消耗：57.94 Mb, 在所有 Python3 提交中击败了 94.59% 的用户
    '''
    cond1 = insurance.groupby('tiv_2015').size().to_dict()
    cond2 = insurance.groupby(['lat', 'lon']).size().to_dict()

    s = 0
    for idx, row in insurance.iterrows():
        if (cond1[row['tiv_2015']] > 1) and (cond2[(row['lat'], row['lon'])]==1):
            s += row['tiv_2016']

    return pd.DataFrame([round(s, 2)], columns=['tiv_2016'])
