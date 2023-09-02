# https://leetcode.cn/problems/students-and-examinations

import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.08.08
    Pass/Error/Bug: 1/1/0
    执行用时：  384 ms, 在所有 Python3 提交中击败了 51.10% 的用户
    内存消耗：61.20 MB, 在所有 Python3 提交中击败了 19.38% 的用户
    '''
    header = pd.merge(students.sort_values('student_id'), subjects, how='cross')
    data = pd.merge(
        students.assign(attended_exams=0),
        examinations,
        on='student_id',
        how='inner'
    ).groupby(['student_id', 'student_name', 'subject_name']).count().reset_index()
    return pd.merge(
        header,
        data,
        on=['student_id', 'student_name', 'subject_name'],
        how='left'
    ).fillna(0).astype({'attended_exams':int}).sort_values(['student_id', 'subject_name'])
