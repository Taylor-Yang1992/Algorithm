class Solution:
    def isValid(self,s):
        if not s:
            return True
        l = []
        d = {"(":")","[":"]","{":"}"}
        for c in s:
            if c in d:
                l.append(c)
            elif c in d.values():
                if (not l) or d[l.pop(-1)] != c:
                    return False
        return not l
