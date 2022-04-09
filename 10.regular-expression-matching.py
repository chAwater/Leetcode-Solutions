# https://leetcode-cn.com/problems/regular-expression-matching/


class Solution1:
    '''
    Date: 2022.04.09
    Pass/Error/Bug: 2/10/2
    执行用时：2456 ms, 在所有 Python3 提交中击败了  5.09% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了 36.20% 的用户
    '''
    def easyMatch(self, s: str, p: str):
        if ('.' in p) or ('*' in p):
            pass
        elif s == p:
            return True
        else:
            return False

        if '*' in p:
            return None
        elif len(s) == len(p):
            for idx in range(len(s)):
                if (p[idx] != '.') and (s[idx] != p[idx]):
                    return False
            return True
        else:
            return False

    def isMatch(self, s: str, p: str) -> bool:
        r = self.easyMatch(s, p)
        if r is not None:
            return r

        s_idx = 0
        p_idx = 0
        while (p_idx < len(p)) and (s_idx < len(s)):

            if '*' not in p[p_idx:p_idx+2]:
                if (p[p_idx] != '.') and (s[s_idx] != p[p_idx]):
                    return False
            else:
                match_tag = 0
                prefix = p[p_idx:p_idx+2].replace('*', '')

                # for n in range(len(s)-s_idx, -1, -1):
                for n in range(0, len(s)-s_idx+1):

                    new_s = s[s_idx:]
                    new_p = prefix * n + p[p_idx+2:]
                    r = self.isMatch(new_s, new_p)
                    if r:
                        s_idx += n
                        p_idx += 1
                        match_tag = 1
                        break

                if match_tag == 1:
                    return True
                else:
                    return False

            p_idx += 1
            s_idx += 1

        rs = s[s_idx:]
        rp = p[p_idx:]
        s_idx = 0
        p_idx = 0

        if rs != '':
            return False

        while p_idx < len(rp):
            sub_p = rp[p_idx]
            if sub_p == '*':
                p_idx += 1
                continue
            else:
                if p_idx+1 < len(rp) and rp[p_idx+1] != '*':
                    return False
                else:
                    if p_idx+1 == len(rp):
                        return False
                    p_idx += 1

        return True


c1 = Solution1()


def test(c):
    f = c.isMatch
    assert f("a", ".*..a*") == False
    assert f("a", "ab*") == True
    assert f("aa", "a*") == True
    assert f("a", "ab..a*") == False
    assert f("aaa", "ab*a*c*a") == True
    assert f("a", "ab*a") == False
    assert f("aaa", "a*") == True
    print('Pass:{}'.format(str(c.__class__)))


test(c1)
