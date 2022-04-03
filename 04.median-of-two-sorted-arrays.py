# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

from typing import List
from math import isclose


class Solution1:
    '''
    Date: 2022.04.03
    Pass/Error/Bug: 1/2/3
    执行用时：  44 ms, 在所有 Python3 提交中击败了 78.14% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了 59.49% 的用户
    '''
    # 递归函数
    def findKth(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # k is 1-based
        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]

        if k == 1:
            return min(nums1[0], nums2[0])

        half_k = k // 2

        if len(nums1) < half_k:
            n1 = nums1[-1]
            n2 = nums2[half_k-1]
            if n1 >= n2:
                nums2 = nums2[half_k:]
                return self.findKth(nums1, nums2, k-half_k)
            else:
                return self.findKth([], nums2, k-len(nums1))
        elif len(nums2) < half_k:
            n1 = nums1[half_k-1]
            n2 = nums2[-1]
            if n1 >= n2:
                return self.findKth(nums1, [], k-len(nums2))
            else:
                nums1 = nums1[half_k:]
                return self.findKth(nums1, nums2, k-half_k)
        else:
            n1 = nums1[half_k-1]
            n2 = nums2[half_k-1]
            if n1 >= n2:
                nums2 = nums2[half_k:]
                return self.findKth(nums1, nums2, k-half_k)
            else:
                nums1 = nums1[half_k:]
                return self.findKth(nums1, nums2, k-half_k)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l1 = len(nums1)
        l2 = len(nums2)

        if (l1 + l2) % 2:
            k = (l1 + l2 + 1) // 2
            return self.findKth(nums1, nums2, k)
        else:
            k1 = (l1 + l2 + 1) // 2
            k2 = (l1 + l2 + 2) // 2
            return (self.findKth(nums1, nums2, k1) + self.findKth(nums1, nums2, k2)) / 2


c1 = Solution1()


def test(c):
    f = c.findMedianSortedArrays
    assert isclose(f([1, 3], [2]), 2), f([1, 3], [2])
    assert isclose(f([2], [1, 3]), 2), f([2], [1, 3])
    assert isclose(f([4], [1, 3]), 3), f([4], [1, 3])
    assert isclose(f([1, 2], [3, 4]), 2.5), f([1, 2], [3, 4])
    assert isclose(f([1], [2]), 1.5), f([1], [2])
    assert isclose(f([], [1, 2]), 1.5), f([], [1, 2])
    assert isclose(f([], [1, 2, 3]), 2), f([], [1, 2, 3])
    assert isclose(f([3], [-2, -1]), -1), f([3], [-2, -1])
    assert isclose(f([1, 3], [2, 7]), 2.5), f([1, 3], [2, 7])
    assert isclose(f([1], [2, 3, 4, 5, 6]), 3.5), f([1], [2, 3, 4, 5, 6])
    print('Pass:{}'.format(str(c.__class__)))


test(c1)
