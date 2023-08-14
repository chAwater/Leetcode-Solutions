# https://leetcode.cn/problems/find-and-replace-in-string


class Solution1:
    '''
    Date: 2023.08.15
    Pass/Error/Bug: 2/1/0
    执行用时：   44 ms, 在所有 Python3 提交中击败了 69.51% 的用户
    内存消耗：15.69 Mb, 在所有 Python3 提交中击败了 78.05% 的用户
    '''
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        new_s = ''

        hash_dict = {}

        for idx in range(len(indices)):
            hash_dict[indices[idx]] = [ sources[idx], targets[idx] ]

        for idx in sorted(hash_dict.keys()):
            new_s = s[:idx]
            break

        gap_idx = idx
        for idx in sorted(hash_dict.keys()):
            sub_s, s_target = hash_dict[idx]
            sub_l = len(sub_s)

            if gap_idx != idx:
                new_s += s[gap_idx:idx]
                gap_idx = idx

            if s[idx:idx+sub_l] == sub_s:
                new_s += s_target
            else:
                new_s += s[idx:idx+sub_l]

            gap_idx = idx+sub_l


        if gap_idx < len(s):
            new_s += s[gap_idx:]

        return new_s
