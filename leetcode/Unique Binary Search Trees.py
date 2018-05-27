class Solution:
    
    def numTrees(self,n):
        if n <= 0:
            return -1
        if n <= 2:
            return n
        l = [0] * n
        l[0] = 1
        l[1] = 2
        for i in range(3,n + 1):
            l[i - 1] = 2 * l[i - 2]
            for j in range(2,i):
                l[i - 1] += l[j - 2] * l[i - j - 1]
        return l[-1]
