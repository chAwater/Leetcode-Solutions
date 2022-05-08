# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/

from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        idict = list( map(lambda x: ''.join(x), zip(*words)) )
        idx_dict = 0
        idx_s = 0
        flag = 0

        rs = []
        c_rs = []

        while idx_s < len(s):
            if s[idx_s] in idict[idx_dict]:
                idx_s += 1
                idx_dict += 1

                if idx_dict == len(idict):
                    flag += 1
                    if flag == len(words):
                        c_rs.append(idx_s-idx_dict*flag)
                        flag = 0
                    idx_dict = 0
            else:
                idx_s += 1
                idx_dict = 0

        return c_rs

