class Solution:
    
    def generate(self,numRows):
        if numRows == 0:
            return []
        if numRows <= 2:
            return [[1]] if numRows == 1 else [[1],[1,1]]
        l = [[1],[1,1]]
        for i in range(3,numRows + 1):
            t = [1] * i
            for j in range(1,i - 1):
                t[j] = l[i - 2][j - 1] + l[i - 2][j]
            l.append(t)
        return l
