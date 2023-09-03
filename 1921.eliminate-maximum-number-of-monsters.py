# https://leetcode.cn/problems/eliminate-maximum-number-of-monsters


class Solution1:
    '''
    Date: 2023.09.03
    Pass/Error/Bug: 1/0/0
    执行用时：  132 ms, 在所有 Python3 提交中击败了 58.57% 的用户
    内存消耗：29.74 Mb, 在所有 Python3 提交中击败了 51.43% 的用户
    '''
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        n = len(dist)
        for idx in range(n):
            time.append(dist[idx] / speed[idx])

        time = sorted(time)

        n = 0
        for i, t in enumerate(time):
            if t <= i:
                break
            else:
                n += 1

        if n == 0:
            return 1
        else:
            return n
