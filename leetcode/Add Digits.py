class Solution:
    
    def addDigits(self,num):
        while num > 9:
            t = 0
            while num > 0:
                t += num % 10
                num = int(num / 10)
            num = t
        return num
