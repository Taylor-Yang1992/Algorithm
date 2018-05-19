class Solution:
    
    def convertToTitle(self,n):
        if n <= 0:
            return "-1"
        d = {i:chr(ord("A") + i - 1) for i in range(1,27)}
        t = ""
        while n > 0:
            mode = n % 26
            n = int(n / 26)
            if mode == 0:
                mode = 26
                n -= 1
            t = d[mode] + t
        return t
