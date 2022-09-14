# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

class Solution1:
    '''
    Date: 2022.04.01
    Pass/Error/Bug: 2/1/0
    执行用时： 444 ms, 在所有 Python3 提交中击败了 10.46% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了 98.56% 的用户
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_l = 0
        i_start = 0
        i_end = 1
        max_l = len(s)

        while True:
            if i_end > max_l:
                return max_sub_l
            sub_s = s[i_start:i_end]
            sub_l = i_end - i_start
            if len(dict(zip(sub_s, [1]*sub_l))) == sub_l:
                if max_sub_l < sub_l:
                    max_sub_l = sub_l
                i_end += 1
            else:
                i_start += 1

class Solution2:
    '''
    Date: 2022.04.01
    Pass/Error/Bug: 1/4/1
    执行用时： 272 ms, 在所有 Python3 提交中击败了 14.79% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 79.35% 的用户
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_l = 0
        i_start = 0
        i_end = 1
        max_l = len(s)
        move_tag = 0
        sub_dict = {}

        while True:
            sub_l = i_end - i_start
            if i_end >= max_l:
                if move_tag and (max_sub_l < sub_l):
                    max_sub_l = sub_l
                if max_l != 1:
                    return max_sub_l
                else:
                    return 1

            if move_tag == 0:
                sub_dict = {}
                sub_s = s[i_start:i_end]
                for n, ss in enumerate(sub_s):
                    sub_dict[ss] = n + i_start
                move_tag = 1
            else:
                last_s = s[i_end]
                if last_s in sub_dict:
                    move_tag = 0
                    i_start = sub_dict[last_s] + 1
                else:
                    sub_dict[last_s] = i_end

                i_end += 1
                if max_sub_l < sub_l:
                    max_sub_l = sub_l


class Solution3:
    '''
    Date: 2022.08.20
    Pass/Error/Bug: 2/2/0
    执行用时：  80 ms, 在所有 Python3 提交中击败了 39.43% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 86.96% 的用户
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_l = 0
        max_l = len(s)

        i_start = 0
        i_end = 1

        while i_end < max_l:
            sub_s = s[i_start:i_end]
            next_s = s[i_end]
            max_sub_l = max(max_sub_l, len(sub_s))
            if next_s in sub_s:
                i_start += sub_s.index(next_s) + 1
            else:
                i_end += 1

        sub_s = s[i_start:i_end]
        max_sub_l = max(max_sub_l, len(sub_s))
        return max_sub_l


class Solution4:
    '''
    Date: 2022.08.21
    Pass/Error/Bug: 2/6/1
    执行用时： 224 ms, 在所有 Python3 提交中击败了 14.87% 的用户
    内存消耗：15.0 MB, 在所有 Python3 提交中击败了 75.79% 的用户
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_l = 0
        max_l = len(s)
        s_dict = {}
        i_start = 0
        i_end = 1

        while i_end <= max_l:
            sub_s = s[i_start:i_end]

            if sub_s[-1] in s_dict:
                i_start = s_dict[sub_s[-1]] + 1
                s_dict = dict(zip(s[i_start:i_end], range(i_start, i_end)))
            else:
                s_dict[sub_s[-1]] = i_end - 1
                max_sub_l = max(max_sub_l, len(sub_s))

            i_end += 1

        return max_sub_l


def test(c):
    f = c.lengthOfLongestSubstring
    assert f('au') == 2, f('au')
    assert f("abcabcbb") == 3, f("abcabcbb")
    assert f('aba') == 2, f('aba')
    assert f('dvdf') == 3, f('dvdf')
    assert f('tmmzuxt') == 5, f('tmmzuxt')
    assert f('bbtablud') == 6, f('bbtablud')
    assert f('') == 0, f('')
    assert f(' ') == 1, f(' ')
    print ('Pass:{}'.format(str(c.__class__)))


c1 = Solution1()
c2 = Solution2()
c3 = Solution3()
c4 = Solution4()

test(c1)
test(c2)
test(c3)
test(c4)
