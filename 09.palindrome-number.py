# https://leetcode-cn.com/problems/palindrome-number/


class Solution1:
    '''
    Date: 2022.04.07
    Pass/Error/Bug: 1/0/0
    执行用时：  56 ms, 在所有 Python3 提交中击败了 85.99% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 80.81% 的用户
    '''
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            s = str(x)
            for i in range(0, len(s)//2):
                if s[i] != s[-1*i-1]:
                    return False

            return True
