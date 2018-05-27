class Solution:
    
    def isHappy(self,n):
        l = []
        while n != 1 and not n in l:
            l.append(n)
            t = 0
            while n > 0:
                t += (n % 10) ** 2
                n = int(n / 10)
            n = t
        return True if n == 1 else False
