class Solution:
    
    def partition(self,s):
        if not s:
            return []
        l = [0] * len(s)
        l[-1] = [[s[-1]]]
        for i in range(len(s) - 2,-1,-1):
            l[i] = []
            for j in range(i,len(s) - 1):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    for item in l[j + 1]:
                        l[i].append([s[i:j + 1]] + item)
            if s[i:] == s[i:][::-1]:
                l[i].append([s[i:]])
        return l[0]
"""
Notes:
  It's convernient to traversal from right to left
"""
