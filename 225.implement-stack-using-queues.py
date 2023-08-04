# https://leetcode.cn/problems/plus-one


class MyStack:
    '''
    Date: 2023.08.04
    Pass/Error/Bug: 1/0/0
    执行用时：   48 ms, 在所有 Python3 提交中击败了 22.37% 的用户
    内存消耗：15.64 MB, 在所有 Python3 提交中击败了 62.97% 的用户
    '''
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        x = self.stack[-1]
        self.stack = self.stack[:-1]
        return x

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
