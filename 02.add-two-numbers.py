# https://leetcode-cn.com/problems/add-two-numbers

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    '''
    Date: 2022.03.30
    Pass/Error/Bug: 1/3/0
    执行用时：72 ms, 在所有 Python3 提交中击败了 15.90% 的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了 35.62% 的用户
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 使用函数递归，增加进位功能
        def addWithCarry(
            l1: Optional[ListNode] = None,
            l2: Optional[ListNode] = None,
            carry: Optional[int] = 0
        ) -> ListNode:
            val1, val2 = 0, 0
            next1, next2 = None, None
            flag1, flag2 = 0, 0

            if l1 is not None:
                val1 = l1.val
                next1 = l1.next
                flag1 = 1
            if l2 is not None:
                val2 = l2.val
                next2 = l2.next
                flag2 = 1

            sum_val = val1 + val2 + carry
            add_val = sum_val // 10
            new_val = sum_val % 10

            if (next1 is None) and (next2 is None):
                if add_val != 0:
                    return ListNode(val=new_val, next=ListNode(val=add_val))
                else:
                    return ListNode(val=new_val)
            elif flag1 + flag2 > 0:
                return ListNode(val=new_val, next=addWithCarry(next1, next2, add_val))
            else:
                return ListNode(val=new_val)

        return addWithCarry(l1, l2)
