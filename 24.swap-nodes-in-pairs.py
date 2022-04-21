# https://leetcode-cn.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        a1 = head
        if a1 is None:
            return None

        a2 = a1.next
        if a2 is None:
            return a1

        a3 = a2.next

        a2.next = a1
        a1.next = self.swapPairs(a3)

        return a2

