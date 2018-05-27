class Solution:
    
    def rb(self,matrix,target,row,f,t,style):
        while f <= t:
            mid = int((f + t) / 2)
            val = matrix[row][mid] if style == 1 else matrix[mid][row]
            if val == target:
                return True
            elif val < target:
                f = mid + 1
            else:
                t = mid - 1
        return False 
    
    def search(self,matrix,target,i,j,m,n):
        if i > m or j > n:
            return False
        if i == m:
            return self.rb(matrix,target,i,j,n,1)
        if j == n:
            return self.rb(matrix,target,j,i,m,2)
        x = int((i + m) / 2)
        y = int((j + n) / 2)
        val = matrix[x][y]
        if val == target:
            return True
        elif val < target:
            return self.search(matrix,target,x + 1,j,m,y) or self.search(matrix,target,i,y + 1,m,n)
        else:
            return self.search(matrix,target,i,j,m,y - 1) or self.search(matrix,target,i,y,x - 1,n)
        
    def searchMatrix(self,matrix,target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False
        return self.search(matrix,target,0,0,m - 1,n - 1)

"""
divide the matrix into four panels and recursively search in the qualified panel
"""
