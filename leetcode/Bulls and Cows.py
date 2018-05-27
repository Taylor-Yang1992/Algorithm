class Solution:
    
    def getHint(self,secret,guess):
        t1 = 0
        t2 = 0
        d = {}
        l = []
        for (_,(s1,s2)) in enumerate(zip(secret,guess)):
            if s1 == s2:
                t1 += 1
            else:
                d[s1] = d[s1] + 1 if s1 in d else 1
                l.append(s2)
        for e in l:
            if e in d and d[e] > 0:
                t2 += 1
                d[e] = d[e] - 1
        return str(t1) + "A" + str(t2) + "B"
