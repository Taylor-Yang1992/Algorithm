class Solution:
    
    def travel(self,grid,i,j,n,m):
        grid[i][j] = 2
        if j - 1 >= 0 and grid[i][j - 1] == "1":
            self.travel(grid,i,j - 1,n,m)
        if j + 1 <= m - 1 and grid[i][j + 1] == "1":
            self.travel(grid,i,j + 1,n,m)
        if i - 1 >= 0 and grid[i - 1][j] == "1":
            self.travel(grid,i - 1,j,n,m)
        if i + 1 <= n - 1 and grid[i + 1][j] == "1":
            self.travel(grid,i + 1,j,n,m)
    
    def numIslands(self,grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        count = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    self.travel(grid,i,j,n,m)
        return count
