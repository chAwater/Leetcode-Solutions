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


class Solution2:
    '''
    Date: 2022.03.31
    Pass/Error/Bug: 1/0/0
    执行用时：68 ms, 在所有 Python3 提交中击败了 25.46% 的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了 12.26% 的用户
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1s = []
        n2s = []

        while l1:
            n1s.append(str(l1.val))
            l1 = l1.next

        while l2:
            n2s.append(str(l2.val))
            l2 = l2.next

        n1s = int(''.join(n1s[::-1]))
        n2s = int(''.join(n2s[::-1]))

        s = n1s + n2s

        prev = None
        for i in str(s):
            out = ListNode(int(i), prev)
            prev = out

        return out


class Solution3:
    '''
    Date: 2022.04.30
    Pass/Error/Bug: 3/3/8
    执行用时：60.0 ms, 在所有 Python3 提交中击败了 72.57% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 82.98% 的用户
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        idx = 0
        carry = 0

        head = ListNode(0)
        cache1 = None
        cache2 = None

        while True:

            if l1:
                v1 = l1.val
                if l1.next:
                    l1 = l1.next
                else:
                    l1 = None
            else:
                v1 = 0

            if l2:
                v2 = l2.val
                if l2.next:
                    l2 = l2.next
                else:
                    l2 = None
            else:
                v2 = 0

            sum_val = v1 + v2 + carry
            add_val = sum_val // 10
            new_val = sum_val % 10

            if sum_val != 0:
                if idx != 0:
                    cache2 = ListNode(new_val)
                    cache1.next = cache2
                    cache1 = cache2
                else:
                    head = ListNode(new_val)
                    cache1 = head

                carry = add_val
                idx += 1
            elif (l1 or l2):
                if idx != 0:
                    cache2 = ListNode(0)
                    cache1.next = cache2
                    cache1 = cache2
                else:
                    head = ListNode(0)
                    cache1 = head

                idx += 1
            else:
                break

        return head
