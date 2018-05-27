class Solution:
    
    def tb(self,n,k,i,c,l,r):
        if i > n:
            return
        if c == k:
            r.append(l + [i])
            return
        for j in range(i + 1,n + 1):
            self.tb(n,k,j,c + 1,l + [i],r)
    
    def combine(self,n,k):
        r = []
        for i in range(1,n + 1):
            self.tb(n,k,i,1,[],r)
        return r
 
 """
 class Solution:
    
    def combine(self,n,k):
        if k == n:
            return [[i for i in range(1,n + 1)]]
        if k == 1:
            return [[i] for i in range(1,n + 1)]
        l = [0] * k
        for i in range(1,n + 1):
            for j in range(min(i,k),0,-1):
                if j == i:
                    l[j - 1] = [[_ for _ in range(1,i + 1)]]
                elif j == 1:
                    l[0] = [[_] for _ in range(1,i + 1)]
                else:
                    for e in l[j - 2]:
                        l[j - 1].append(e + [i])
        return l[k - 1]
 """
 """
 the first is traceback solution while the second is dynamic solution
 """
