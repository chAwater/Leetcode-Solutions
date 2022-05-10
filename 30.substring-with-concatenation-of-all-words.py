# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/

from typing import List


class Solution1:
    '''
    Date: 2022.05.11
    Pass/Error/Bug: 1/2/0
    执行用时： 376 ms, 在所有 Python3 提交中击败了 66.67% 的用户
    内存消耗：15.6 MB, 在所有 Python3 提交中击败了 13.59% 的用户
    '''
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        total_s = ''.join(words)
        window_l = len(total_s)
        n_words = len(words)
        l_word = window_l // n_words
        rs = []

        wdict = {}
        for w in words:
            if w in wdict:
                wdict[w] += 1
            else:
                wdict[w] = 1

        for window_i in range(len(s)-window_l+1):
            sub_s = s[window_i : window_i+window_l]
            cdict = dict(zip(words, [0]*n_words))
            good_flag = 1
            for word_i in range(0, window_l, l_word):
                sub_w = sub_s[word_i:word_i+l_word]
                if sub_w in cdict:
                    cdict[sub_w] += 1
                    if cdict[sub_w] > wdict[sub_w]:
                        good_flag = 0
                        break
                else:
                    good_flag = 0
                    break
            if good_flag:
                rs.append(window_i)

        return rs
