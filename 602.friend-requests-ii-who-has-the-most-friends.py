# https://leetcode.cn/problems/friend-requests-ii-who-has-the-most-friends

import pandas as pd


def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    '''
    Date: 2023.09.04
    Pass/Error/Bug: 1/0/0
    执行用时：  256 ms, 在所有 Python3 提交中击败了 96/83% 的用户
    内存消耗：58.94 Mb, 在所有 Python3 提交中击败了 65.08% 的用户
    '''
    return (
        (
            pd.concat(
                [
                    request_accepted,
                    request_accepted.rename(columns={'requester_id':'accepter_id', 'accepter_id':'requester_id'})
                ]
            )
            .groupby('requester_id').size()
        ).reset_index()
        .rename(columns={'requester_id':'id', 0:'num'})
        .sort_values('num').tail(1)
    )
