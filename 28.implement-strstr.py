# https://leetcode-cn.com/problems/implement-strstr/


class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        if length == 0:
            return 0

        for idx in range(len(haystack)):
            if haystack[idx:idx+length] == needle:
                return idx

        return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
