# https://leetcode.cn/problems/classes-more-than-5-students

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.07
    Pass/Error/Bug: 1/1/0
    执行用时：  256 ms, 在所有 Python3 提交中击败了 62.80% 的用户
    内存消耗：60.70 Mb, 在所有 Python3 提交中击败了 50.56% 的用户
    '''
    return courses.groupby('class').count().query('student>=5').reset_index().loc[:, ['class']]
