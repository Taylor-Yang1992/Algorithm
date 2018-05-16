class Solution:
    
    def getRow(self,rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex <= 1:
            return [1,1]
        l = [1] * (rowIndex + 1)
        for i in range(2,rowIndex + 1):
            for j in range(i - 1, 0,-1):
                l[j] += l[j - 1]
        return l
