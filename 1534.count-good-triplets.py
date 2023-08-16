# https://leetcode.cn/problems/count-good-triplets/


class Solution1:
    '''
    Date: 2023.08.17
    Pass/Error/Bug: 1/0/0
    执行用时：  612 ms, 在所有 Python3 提交中击败了 19.25% 的用户
    内存消耗：15.52 Mb, 在所有 Python3 提交中击败了 93.31% 的用户
    '''
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        length = len(arr)
        for i in range(0, length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1

        return count
