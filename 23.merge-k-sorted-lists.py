# https://leetcode-cn.com/problems/merge-k-sorted-lists/

from typing import List, Optional


# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        handles = []
        values = []
        for l in lists:
            if l is None:
                continue
            else:
                handles.append(l)
                values.append(l.val)
        
        if len(handles) == 0:
            return None

        head = self.mergeKLists([h.next for h in handles])

        for v in sorted(values, reverse=True):
            head = ListNode(val=v, next=head)

        return head


