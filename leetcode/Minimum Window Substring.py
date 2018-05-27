class Solution:
    
    def minWindow(self,s,t):
        if not s or len(s) < len(t):
            return ""
        d = {}
        for e in t:
            d[e] = d.get(e,0) + 1
        n = len(d)
        pre = 0
        l = len(s) + 1
        result = ""
        for i in range(len(s)):
            if s[i] in d:
                v = d[s[i]]
                d[s[i]] = v - 1
                if v == 1:
                    n -= 1
                if n == 0:
                    j = pre
                    while n == 0:
                        if s[j] in d:
                            v = d[s[j]]
                            d[s[j]] = v + 1
                            if v == 0:
                                n += 1
                        j += 1
                    pre = j
                    if i - j + 2 < l:
                        l = i - j + 2
                        result = s[j - 1:i + 1]
        return result
