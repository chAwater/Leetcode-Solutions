# https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range


class Solution1:
    '''
    Date: 2023.08.24
    Pass/Error/Bug: 1/1/0
    执行用时：   40 ms, 在所有 Python3 提交中击败了 93.12% 的用户
    内存消耗：15.69 Mb, 在所有 Python3 提交中击败了 90.06% 的用户
    '''
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for word in words[left:right+1]:
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                count += 1

        return count
