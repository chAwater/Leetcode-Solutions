# https://leetcode.cn/problems/shuffle-the-array


class Solution1:
    '''
    Date: 2023.08.19
    Pass/Error/Bug: 1/0/0
    执行用时：   40 ms, 在所有 Python3 提交中击败了 82.26% 的用户
    内存消耗：15.86 Mb, 在所有 Python3 提交中击败了 15.20% 的用户
    '''
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result += [nums[i], nums[n+i]]

        return result

class Solution2:
    '''
    Date: 2023.08.19
    Pass/Error/Bug: 1/0/0
    执行用时：   44 ms, 在所有 Python3 提交中击败了 65.03% 的用户
    内存消耗：15.82 Mb, 在所有 Python3 提交中击败了 31.76% 的用户
    '''
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums
