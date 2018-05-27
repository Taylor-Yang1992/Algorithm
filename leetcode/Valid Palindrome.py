class Solution:
    
    def isPalindrome(self,s):
        if not s:
            return True
        l = []
        for c in s:
            if (c >= "A" and c <= "Z") or (c >= "a" and c <= "z"):
                l.append(c.lower())
            elif c >= "0" and c <= "9":
                l.append(c)
        if not l:
            return True
        return l == l[::-1]
