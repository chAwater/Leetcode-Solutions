# https://leetcode-cn.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    '''
    Date: 2022.04.26
    Pass/Error/Bug: 2/0/0
    执行用时：  36 ms, 在所有 Python3 提交中击败了 71.34% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 18.49% 的用户
    '''
    def swapPairs(self, head: ListNode) -> ListNode:

        if (head is None) or (head.next is None):
            return head
        else:
            a1 = head
            a2 = head.next
            a1.next = self.swapPairs(a2.next)
            a2.next = a1

        return a2
