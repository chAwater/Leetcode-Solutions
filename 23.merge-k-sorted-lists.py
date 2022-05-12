# https://leetcode-cn.com/problems/merge-k-sorted-lists/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    '''
    Date: 2022.04.25
    Pass/Error/Bug: 1/1/0
    执行用时：2052 ms, 在所有 Python3 提交中击败了 21.44% 的用户
    内存消耗：18.1 MB, 在所有 Python3 提交中击败了 48.20% 的用户
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        handles = []
        values = []
        for ls in lists:
            if ls is None:
                continue
            else:
                handles.append(ls)
                values.append(ls.val)

        if len(handles) == 0:
            return None

        rs = []
        ridx = 0
        while len(handles) > 0:
            min_idx = 0
            min_v = values[min_idx]

            for idx in range(len(values)):
                if min_v > values[idx]:
                    min_idx = idx
                    min_v = values[min_idx]

            rs.append(handles[min_idx])

            if ridx == 0:
                ridx += 1
            else:
                rs[ridx-1].next = rs[ridx]
                ridx += 1

            if handles[min_idx].next:
                handles[min_idx] = handles[min_idx].next
                values[min_idx] = handles[min_idx].val
            else:
                handles.pop(min_idx)
                values.pop(min_idx)

        return rs[0]
