class Solution:
    
    def isIsomorphic(self,s,t):
        if not s or s == t:
            return True
        d1 = {}
        d2 = {}
        for (_,(e1,e2)) in enumerate(zip(s,t)):
            if not e1 in d1:
                if not e2 in d2:
                    d1[e1] = e2
                    d2[e2] = e1
                else:
                    if d2[e2] != e1:
                        return False
            else:
                if d1[e1] != e2:
                    return False
        return True
