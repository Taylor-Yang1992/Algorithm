class Solution:
    
    def tb(self,matrix,i,m,n,l):
        if m <= 0 or n <= 0:
            return
        if m == 1 or n == 1:
            if m == 1:
                l.extend(matrix[i][i:n + i])
                return
            if n == 1:
                j = i
                for _ in range(m):
                    l.append(matrix[j][i])
                    j += 1
                return
        l.extend(matrix[i][i:n + i - 1])
        j = i
        for _ in range(m - 1):
            l.append(matrix[j][n + i - 1])
            j += 1
        l.extend(matrix[i + m - 1][i + n - 1:i:-1])
        j = i + m - 1
        for _ in range(m - 1):
            l.append(matrix[j][i])
            j -= 1
        self.tb(matrix,i + 1,m - 2,n - 2,l)
    
    def spiralOrder(self,matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        l = []
        self.tb(matrix,0,m,n,l)
        return l

"""
just do it step by step
from left to right,from top to bottom,from right to left and from bottom to top
doing recursively
"""
