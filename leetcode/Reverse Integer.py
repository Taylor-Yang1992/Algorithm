class Solution:
    
    def reverse(self,x):
        if x == 0:
            return 0
        sign = x > 0
        x = x if sign else -x
        v = 0
        while x > 0:
            v = v * 10 + x % 10
            x = int(x / 10)
        return (v if v <= 2 ** 31 - 1 else 0) if sign else (-v if v <= 2 ** 31 else 0)
