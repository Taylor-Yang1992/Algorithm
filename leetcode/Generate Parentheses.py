class Solution:
    def generateParenthesis(self,n):
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        l = [[] for i in range(n)]
        l[0] = ["()"]
        for i in range(2,n + 1):
            l[i - 1] = ["(" + s + ")" for s in l[i - 2]]
            for j in range(1,i):
                t = [s1 + s2 for s1 in l[j - 1] for s2 in l[i - j - 1]]
                for item in t:
                    if not item in l[i - 1]:
                        l[i - 1].append(item)
        return l[n - 1]
