# https://leetcode-cn.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.say( self.countAndSay(n-1) )
        
    def say(self, inputs: str) -> str:
        if inputs == '1':
            return '11'
        else:
            res = ''
            pre = inputs[0]
            count = 1
            for idx in range(1, len(inputs)):
                sub = inputs[idx]
                if sub == pre:
                    count += 1
                else:
                    res += str(count) + pre
                    pre = sub
                    count = 1
    
            res += str(count) + pre
            return res

