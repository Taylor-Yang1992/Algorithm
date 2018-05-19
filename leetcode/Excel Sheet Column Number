class Solution:
    
    def titleToNumber(self,s):
        if not s:
            return 0
        d = {chr(ord("A") + i - 1):i for i in range(1,27)}
        t = 0
        for c in s:
            t = t * 26 + d[c]
        return t
