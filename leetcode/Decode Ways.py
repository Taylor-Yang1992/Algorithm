class Solution:
    
    def numDecodings(self,s):
        if not s or s[0] == "0":
            return 0
        s = "1" + s
        pre = 1
        cur = 1
        for i in range(2,len(s)):
            ne = 0
            if int(s[i]) in range(1,10):
                ne += cur
            if int(s[i - 1:i + 1]) in range(10,27):
                ne += pre
            if ne == 0:
                return 0
            else:
                pre,cur = cur,ne
        return cur
