class Solution:
    
    def reverseWords(self,s):
        if not s:
            return s
        l = []
        for item in s.split()[::-1]:
            if item:
                l.append(item)
        return " ".join(l)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
