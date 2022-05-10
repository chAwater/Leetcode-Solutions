# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/

from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        total_s = ''.join(words)
        window_l = len(total_s)
        n_words = len(words)
        l_word = window_l // n_words
        rs = []

        for window_i in range(len(s)-window_l+1):
            sub_s = s[window_i : window_i+window_l]
            wdict = dict(zip(words, [0]*n_words))
            good_flag = 1
            for word_i in range(0, window_l, l_word):
                sub_w = sub_s[word_i:word_i+l_word]
                if sub_w in wdict:
                    if wdict[sub_w] == 0:
                        wdict[sub_w] = 1
                    else:
                        good_flag = 0
                        break
                else:
                    good_flag = 0
                    break
            if good_flag:
                rs.append(window_i)

        return rs



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

