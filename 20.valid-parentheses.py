# https://leetcode-cn.com/problems/valid-parentheses/


class Solution1:
    '''
    Date: 2022.04.20
    Pass/Error/Bug: 1/0/2
    执行用时：  36 ms, 在所有 Python3 提交中击败了 74.15% 的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了  5.14% 的用户
    '''
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        tag_dict = {
            '(' : 'a',
            ')' : 'a',
            '[' : 'b',
            ']' : 'b',
            '{' : 'c',
            '}' : 'c',
        }
        tag_flag = {
            '(' : 0,
            ')' : 1,
            '[' : 0,
            ']' : 1,
            '{' : 0,
            '}' : 1,
        }
        stack_s = []
        for sub_s in s:
            if tag_flag[sub_s]:
                # Pair with last input
                if (len(stack_s) != 0) and (stack_s[-1] == tag_dict[sub_s]):
                    stack_s.pop()
                    continue
                else:
                    return False
            else:
                stack_s.append(tag_dict[sub_s])

        if len(stack_s) != 0:
            return False
        else:
            return True
