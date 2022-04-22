# https://leetcode-cn.com/problems/merge-two-sorted-lists/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    '''
    Date: 2022.04.22
    Pass/Error/Bug: 1/1/0
    执行用时：  48 ms, 在所有 Python3 提交中击败了 15.45% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了  5.29% 的用户
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            return ListNode(
                val=list1.val,
                next=self.mergeTwoLists(list1.next, list2)
            )
        else:
            return ListNode(
                val=list2.val,
                next=self.mergeTwoLists(list1, list2.next)
            )
