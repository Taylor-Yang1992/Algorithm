class Solution:
    
    def trailingZeroes(self,n):
        if n == 0:
            return 0
        t = 0
        while n > 0:
            n = int(n / 5)
            t += n
        return t
