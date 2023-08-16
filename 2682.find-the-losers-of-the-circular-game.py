# https://leetcode.cn/problems/find-the-losers-of-the-circular-game/


class Solution1:
    '''
    Date: 2023.08.16
    Pass/Error/Bug: 1/0/0
    执行用时：   52 ms, 在所有 Python3 提交中击败了 51.94% 的用户
    内存消耗：15.77 Mb, 在所有 Python3 提交中击败了 14.60% 的用户
    '''
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        count_dict = {}
        i = 0
        for idx in range(n):
            i = (i + idx*k) % n
            if i in count_dict:
                break
            else:
                count_dict[i] = 1

        return [ i+1 for i in range(n) if i not in count_dict ]
