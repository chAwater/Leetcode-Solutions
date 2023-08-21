# https://leetcode.cn/problems/maximize-distance-to-closest-person/


class Solution1:
    '''
    Date: 2023.08.22
    Pass/Error/Bug: 1/2/0
    执行用时： 1084 ms, 在所有 Python3 提交中击败了 5.05% 的用户
    内存消耗：17.75 Mb, 在所有 Python3 提交中击败了 5.05% 的用户
    '''
    def maxDistToClosest(self, seats: List[int]) -> int:
        total_length = len(seats) - 1
        seq_seats = ''.join([str(i) for i in seats])
        match_str = '0'*total_length

        max_dist = []

        while total_length > 1:
            match_str = '0'*total_length
            if match_str in seq_seats:
                if seq_seats.startswith(match_str) or seq_seats.endswith(match_str):
                    max_dist.append(total_length)
                elif total_length % 2 == 0:
                    max_dist.append(total_length // 2)
                else:
                    max_dist.append(total_length // 2 + 1)

            total_length -= 1

        if len(max_dist) == 0:
            return 1
        else:
            return max(max_dist)
