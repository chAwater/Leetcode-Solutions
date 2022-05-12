# https://leetcode-cn.com/problems/divide-two-integers/


class Solution1:
    '''
    Date: 2022.05.05
    Pass/Error/Bug: 1/2/4
    执行用时：  52 ms, 在所有 Python3 提交中击败了 14.97% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 69.95% 的用户
    '''
    def divbysub(self, dividend: int, divisor: int) -> tuple[int, int]:
        ds = 0
        rs = 0

        while dividend >= divisor:
            dividend = dividend - divisor
            ds += 1

        rs = dividend

        return (ds, rs)

    def divide(self, dividend: int, divisor: int) -> int:
        flag = 0
        if dividend < 0:
            flag += 1

        if divisor < 0:
            flag += 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            if flag == 1:
                r = 0 - dividend
            else:
                r = dividend

            if r > 2**31-1:
                return 2**31-1
            else:
                return r

        dss = ''
        rs = ''
        for s_dividend in str(dividend):
            (ds, rs) = self.divbysub(int(rs + s_dividend), divisor)
            rs = str(rs)
            ds = str(ds)
            dss += ds

        if flag == 1:
            return 0 - int(dss)
        else:
            return int(dss)
