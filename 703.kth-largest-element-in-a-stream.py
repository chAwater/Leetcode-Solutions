# https://leetcode.cn/problems/kth-largest-element-in-a-stream/


class KthLargest:
    '''
    Date: 2023.08.07
    Pass/Error/Bug: 1/0/0
    执行用时： 1128 ms, 在所有 Python3 提交中击败了 7.61% 的用户
    内存消耗：20.39 Mb, 在所有 Python3 提交中击败了 7.08% 的用户
    '''
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)


    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
