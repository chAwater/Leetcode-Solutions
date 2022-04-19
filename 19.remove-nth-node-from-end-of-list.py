# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    '''
    Date: 2022.04.19
    Pass/Error/Bug: 1/1/1
    执行用时：  32 ms, 在所有 Python3 提交中击败了 92.06% 的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了 97.39% 的用户
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        counter = 0  # 1-based
        nodelist = []

        if (head.next is None) and (n == 1):
            return None

        while head.next:
            nodelist.append(head)
            head = head.next
            counter += 1

        nodelist.append(head)
        counter += 1

        if counter == n:
            return nodelist[1]

        fidx = counter - n
        if fidx + 1 >= len(nodelist):
            nodelist[fidx-1].next = None
        else:
            nodelist[fidx-1].next = nodelist[fidx+1]

        return nodelist[0]
