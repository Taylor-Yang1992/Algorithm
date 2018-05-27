class Solution:

	def minPathSum(self,grid):
		m = len(grid)
		n = len(grid[0])
		pre = [0] * n
		t = 0
		for i in range(n):
			pre[i] = t + grid[0][i]
			t += grid[0][i]
		for i in range(1,m):
			cur = [0] * n
			for j in range(n):
				cur[j] = pre[j] + grid[i][j] if j == 0 else min(pre[j],cur[j - 1]) + grid[i][j]
			pre = cur
		return pre[-1]
