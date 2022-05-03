# https://leetcode-cn.com/problems/4sum/

from typing import List


class Solution1:
    '''
    Date: 2022.05.02
    Pass/Error/Bug: 1/6/3
    执行用时：  96 ms, 在所有 Python3 提交中击败了 80.39% 的用户
    内存消耗：19.1 MB, 在所有 Python3 提交中击败了  5.01% 的用户
    '''
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ndict = {}
        for n in nums:
            if n in ndict:
                ndict[n] += 1
            else:
                ndict[n] = 1

        unums = sorted(ndict.keys())

        rs = []

        vdict = {}
        rdict = {}
        for idx1 in range(len(unums)):
            v1 = unums[idx1]
            if (ndict[v1] >= 4) and (v1 * 4 == target):
                rs.append( [v1] * 4 )
            elif ndict[v1] >= 3:
                res = target - v1*3
                if (res in ndict) and (res != v1):
                    rs.append( [v1] * 3 + [res] )
            elif ndict[v1] >= 2:
                if v1*2 in vdict:
                    vdict[v1*2].append( (idx1,) )
                else:
                    vdict[v1*2] = [(idx1,)]

            for idx2 in range(idx1+1, len(unums)):
                v2 = unums[idx2]
                if v1 + v2 in vdict:
                    vdict[v1 + v2].append((idx1, idx2))
                else:
                    vdict[v1 + v2] = [(idx1, idx2)]

        for sum2 in vdict.keys():
            res = target - sum2

            if res in vdict:
                for a in vdict[sum2]:
                    for b in vdict[res]:
                        if len(a) + len(b) == 4:
                            (idx1, idx2), (idx3, idx4) = a, b
                            if len( set([idx1, idx2, idx3, idx4]) ) == 4:
                                rdict[':'.join(map(str, sorted([unums[idx1], unums[idx2], unums[idx3], unums[idx4]])))] = 1
                            elif len( set([idx1, idx2, idx3, idx4]) ) == 3:
                                if (idx1 in (idx3, idx4)):
                                    if (ndict[unums[idx1]] < 2):
                                        continue
                                elif (idx2 in (idx3, idx4)):
                                    if (ndict[unums[idx2]] < 2):
                                        continue
                                rdict[':'.join(map(str, sorted([unums[idx1], unums[idx2], unums[idx3], unums[idx4]])))] = 1

                            elif len( set([idx1, idx2, idx3, idx4]) ) == 2:
                                if (ndict[unums[idx1]] < 2) or (ndict[unums[idx2]] < 2):
                                    continue

                                rdict[':'.join(map(str, sorted([unums[idx1], unums[idx2], unums[idx3], unums[idx4]])))] = 1
                        else:
                            if (len(a) == 1) and (len(b) == 2) and (a[0] not in b):
                                rdict[':'.join(map(str, sorted([unums[a[0]], unums[a[0]], unums[b[0]], unums[b[1]]])))] = 1
                            elif (len(a) == 2) and (len(a) == 1) and (b[0] not in a):
                                rdict[':'.join(map(str, sorted([unums[b[0]], unums[b[0]], unums[a[0]], unums[a[1]]])))] = 1
                            elif (len(a) == 1) and (len(b) == 1) and (a[0] != b[0]):
                                rdict[':'.join(map(str, sorted([unums[a[0]], unums[a[0]], unums[b[0]], unums[b[0]]])))] = 1

        for r in rdict.keys():
            r = list(map(int, r.split(':')))
            rs.append(r)

        return rs
