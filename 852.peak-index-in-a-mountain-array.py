# https://leetcode.cn/problems/peak-index-in-a-mountain-array


class Solution1:
    '''
    Date: 2023.08.24
    Pass/Error/Bug: 2/0/0
    执行用时：   44 ms, 在所有 Python3 提交中击败了 95.66% 的用户
    内存消耗：28.05 Mb, 在所有 Python3 提交中击败了  5.07% 的用户
    '''
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        idx = length//2

        if (length == 1) or (idx + 1 >= length) or (idx - 1 < 0):
            return idx

        if arr[idx]>arr[idx+1] and arr[idx]>arr[idx-1]:
            return idx
        elif arr[idx-1]>arr[idx]>arr[idx+1]:
            return self.peakIndexInMountainArray(arr[:idx])
        elif arr[idx-1]<arr[idx]<arr[idx+1]:
            return idx + self.peakIndexInMountainArray(arr[idx:])
        else:
            raise ValueError


class Solution2:
    '''
    Date: 2023.08.24
    Pass/Error/Bug: 1/0/0
    执行用时：   56 ms, 在所有 Python3 提交中击败了 63.09% 的用户
    内存消耗：27.26 Mb, 在所有 Python3 提交中击败了 19.54% 的用户
    '''
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))
