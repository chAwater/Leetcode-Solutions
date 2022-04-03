# https://leetcode-cn.com/problems/longest-palindromic-substring


class Solution1:
    '''
    Date: 2022.04.03
    Pass/Error/Bug: 2/2/4
    执行用时：2324 ms, 在所有 Python3 提交中击败了 53.41% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了 72.08% 的用户
    '''
    def longestPalindrome(self, s: str) -> str:

        tdict = {}  # alphabet
        rdict = {}  # save the repeat alphabet
        ndict = {}  # save the min distance of repeat

        for i, sub_s in enumerate(s):
            # Find repeat
            if sub_s in tdict:
                if sub_s in rdict:
                    rdict[sub_s] += [i]
                    distance = i - tdict[sub_s]
                    if distance < ndict[sub_s]:
                        ndict[sub_s] = distance
                else:
                    rdict[sub_s] = [tdict[sub_s], i]
                    ndict[sub_s] = i - tdict[sub_s]

            tdict[sub_s] = i

        if len(rdict) == 0:
            return sub_s
        else:
            candidate = []
            for sub_s, distance in ndict.items():
                if distance <= 2:
                    candidate.append(sub_s)
            results = sub_s

            for sub_s in candidate:
                for idx in rdict[sub_s]:
                    if (idx + 1 < len(s)) and (s[idx] == s[idx+1]):
                        for n in range(999):
                            if (idx - n >= 0) and (idx + 1 + n < len(s)) and (s[idx-n] == s[idx+1+n]):
                                tmp = s[idx-n:idx+2+n]
                                if len(tmp) > len(results):
                                    results = tmp
                            else:
                                break

                    if (idx + 2 < len(s)) and (s[idx] == s[idx+2]):
                        for n in range(999):
                            if (idx - n >= 0) and (idx + 2 + n < len(s)) and (s[idx-n] == s[idx+2+n]):
                                tmp = s[idx-n:idx+3+n]
                                if len(tmp) > len(results):
                                    results = tmp
                            else:
                                break

            return results
