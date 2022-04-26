# https://leetcode-cn.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution1:
    '''
    Date: 2022.04.26
    Pass/Error/Bug: 1/0/0
    执行用时：  52 ms, 在所有 Python3 提交中击败了  6.02% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 25.93% 的用户
    '''
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

