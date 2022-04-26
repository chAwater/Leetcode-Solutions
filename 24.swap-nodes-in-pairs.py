# https://leetcode-cn.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    '''
    Date: 2022.04.26
    Pass/Error/Bug: 3/0/0
    执行用时：  32 ms, 在所有 Python3 提交中击败了 89.624% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了   7.60% 的用户
    '''
    def swapPairs(self, head: ListNode) -> ListNode:

        if (head is None) or (head.next is None):
            return head
        else:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head

        return tmp
