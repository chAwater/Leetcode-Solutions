# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    '''
    Date: 2022.05.03
    Pass/Error/Bug: 1/0/0
    执行用时：  40 ms, 在所有 Python3 提交中击败了 96.18% 的用户
    内存消耗：16.0 MB, 在所有 Python3 提交中击败了 40.35% 的用户
    '''
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        rs = []
        caches = []
        counter = 0

        while head:

            caches.append(head)
            counter += 1

            if counter == k:
                caches.reverse()

                for tmp in caches:
                    rs.append(tmp)

                counter = 0
                caches = []

            head = head.next

        rs[-1].next = rs[-k].next

        for idx in range(len(rs)-1):
            rs[idx].next = rs[idx+1]

        return rs[0]
