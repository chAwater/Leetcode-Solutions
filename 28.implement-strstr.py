# https://leetcode-cn.com/problems/implement-strstr/


class Solution1:
    '''
    Date: 2022.04.29
    Pass/Error/Bug: 1/0/0
    执行用时：  36 ms, 在所有 Python3 提交中击败了 85.23% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 87.27% 的用户
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        if length == 0:
            return 0

        for idx in range(len(haystack)):
            if haystack[idx:idx+length] == needle:
                return idx

        return -1


class Solution2:
    '''
    Date: 2022.04.29
    Pass/Error/Bug: 1/0/0
    执行用时：  32 ms, 在所有 Python3 提交中击败了 94.31% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 87.13% 的用户
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
