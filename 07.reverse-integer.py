# https://leetcode-cn.com/problems/reverse-integer/

class Solution1:
    '''
    Date: 2022.04.05
    Pass/Error/Bug: 1/3/0
    执行用时：  36 ms, 在所有 Python3 提交中击败了 76.48% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 77.08% 的用户
    '''
    def reverse(self, x: int) -> int:
        tag = 1 if x > 0 else -1
        o = tag * int(str(tag * x)[::-1])
        if -2**31 <= o <= 2**31-1:
            return o
        else:
            return 0


class Solution2:
    '''
    Date: 2022.04.05
    Pass/Error/Bug: 1/0/0
    执行用时：  36 ms, 在所有 Python3 提交中击败了 76.48% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 18.03% 的用户
    '''
    def reverse(self, x: int) -> int:
        if x == 0 or x == -2**31:
            return 0

        if x > 0:
            mtag = 1
        else:
            mtag = -1
            x = abs(x)

        o = 0
        i = 0

        maxint = 2**31

        while x != 0:
            if (i >= 8):
                if o > maxint // 10:
                    return 0
                if o == maxint // 10:
                    if x % 10 > maxint % 10:
                        return 0
                    if x % 10 == maxint % 10:
                        if mtag == 1:
                            return 0

            o = o * 10 + x % 10
            x = x // 10
            i += 1

        return mtag * o
