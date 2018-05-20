class Solution:
    
    def rangeBitwiseAnd(self,m,n):
        t = 1
        while m != 0 and m != n:
            m = int(m / 2)
            n = int(n / 2)
            t *= 2
        return m * t
