# https://leetcode-cn.com/problems/3sum/

from typing import List


class Solution:
    '''
    Date: 2022.04.16
    Pass/Error/Bug: 1/0/0
    执行用时：5136 ms, 在所有 Python3 提交中击败了  5.03% 的用户
    内存消耗：27.0 MB, 在所有 Python3 提交中击败了  5.01% 的用户
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Hash index for number positions
        '''
        # Build hash for index
        # Save as a index list if the number is duplicated
        # Eg. { num1 : pos, num2 : [pos1, pos2] }
        v_dict = {}
        for i, v in enumerate(nums):
            if v in v_dict:
                last = v_dict[v]
                if type(last) == list:
                    v_dict[v] += [i]
                else:
                    v_dict[v] = [last, i]
            else:
                v_dict[v] = i

        rs = []
        # Check the hash to find the target
        for v1, idxs1 in v_dict.items():
            v2 = target - v1
            if v1 == v2:
                if (type(idxs1) == list) and (len(idxs1) >= 2):
                    rs.append([nums[idxs1[0]], nums[idxs1[1]]])
            elif v2 in v_dict:
                idxs2 = v_dict[v2]
                idx1 = idxs1[0] if type(idxs1) == list else idxs1
                idx2 = idxs2[0] if type(idxs2) == list else idxs2
                rs.append([nums[idx1], nums[idx2]])
            else:
                continue

        return rs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        rs = []
        for idx, n in enumerate(nums):
            target = -1 * n
            candidate = nums[:idx] + nums[idx+1:]
            for two_r in self.twoSum(candidate, target):
                three_r = two_r + [n]
                rs.append(three_r)

        r_dict = {}
        for r in rs:
            r_str = ':'.join(map(str, sorted(r)))
            r_dict[r_str] = 1

        rs = []
        for r in r_dict.keys():
            r = list(map(int, r.split(':')))
            rs.append(r)

        return rs


class Solution2:
    '''
    Date: 2022.04.14
    Pass/Error/Bug: 1/6/4
    执行用时：3904 ms, 在所有 Python3 提交中击败了  8.33% 的用户
    内存消耗：19.0 MB, 在所有 Python3 提交中击败了  5.01% 的用户
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        ls = len(nums)
        rs = []
        flag_dict = {}

        upper = len(nums) - 1
        idx1, idx2, idx3 = 0, 1, 2

        for idx1 in range(ls):
            idx2 = idx1 + 1
            idx3 = ls - 1

            if nums[idx1] > 0:
                break

            while idx2 < idx3:
                candidate = [ nums[idx1], nums[idx2], nums[idx3] ]
                sum3 = sum(candidate)

                if sum3 > 0:
                    idx3 -= 1
                elif sum3 < 0:
                    idx2 += 1
                else:
                    flag = ':'.join([str(i) for i in candidate])
                    if flag not in flag_dict:
                        rs.append(candidate)
                        flag_dict[flag] = 1
                    idx2 += 1
                    idx3 -= 1

        return rs

