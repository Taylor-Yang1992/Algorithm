class Solution:
    
    def wordPattern(self,pattern,str):
        if not pattern and not str:
            return True
        if not pattern or not str:
            return False
        words = str.split()
        if len(pattern) != len(words):
            return False
        d1 = {}
        d2 = {}
        for (_,(p,s)) in enumerate(zip(pattern,words)):
            if p in d1:
                if d1[p] != s:
                    return False
            else:
                if not s in d2:
                    d1[p] = s
                    d2[s] = p
                else:
                    return False
        return True
