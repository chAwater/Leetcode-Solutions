# https://leetcode.cn/problems/multiply-strings/



class Solution2:
    '''
    Date: 2022.05.14
    Pass/Error/Bug: 1/0/0
    执行用时：  40 ms, 在所有 Python3 提交中击败了 85.24% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 58.44% 的用户
    '''
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))
