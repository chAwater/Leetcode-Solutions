# https://leetcode-cn.com/problems/4sum/

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        vdict = {}
        rdict = {}
        for idx1 in range(len(nums)):
            for idx2 in range(idx1+1, len(nums)):
                sum2 = nums[idx1] + nums[idx2]
                if sum2 in vdict:
                    vdict[sum2].append((idx1, idx2))
                else:
                    vdict[sum2] = [(idx1, idx2)]

        for sum2 in vdict.keys():
            res = target - sum2
            if res in vdict:
                for (idx1, idx2) in vdict[sum2]:
                    for (idx3, idx4) in vdict[res]:
                        if len( set([idx1, idx2, idx3, idx4]) ) == 4:
                            rdict[':'.join(map(str, sorted([nums[idx1], nums[idx2], nums[idx3], nums[idx4]])))] = 1

        rs = []
        for r in rdict.keys():
            r = list(map(int, r.split(':')))
            rs.append(r)
    
        return rs

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        vdict = {}
        rdict = {}
        for idx1 in range(len(nums)):
            for idx2 in range(idx1+1, len(nums)):
                sum2 = nums[idx1] + nums[idx2]
                if sum2 in vdict:
                    vdict[sum2].append((idx1, idx2))
                else:
                    vdict[sum2] = [(idx1, idx2)]

        for idx1 in range(len(nums)):
            for idx2 in range(idx1+1, len(nums)):
                res = target - nums[idx1] - nums[idx2]
                if res in vdict:
                    for (idx3, idx4) in vdict[res]:
                        if len(set([idx1, idx2, idx3, idx4])) == 4:
                            rdict[':'.join(map(str, sorted([nums[idx1], nums[idx2], nums[idx3], nums[idx4]])))] = 1

        rs = []
        for r in rdict.keys():
            r = list(map(int, r.split(':')))
            rs.append(r)

        return rs
