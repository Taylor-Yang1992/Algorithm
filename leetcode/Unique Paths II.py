class Solution:

	def uniquePathsWithObstacles(self,obstacleGrid):
		if obstacleGrid[0][0] == 1:
			return 0
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])
		pre = [1] * n
		for i in range(1,n):
			if obstacleGrid[0][i] == 1:
				pre[i] = 0
				for j in range(i + 1,n):
					pre[j] = 0
				break
		for i in range(1,m):
			cur = [0] * n
			for j in range(n):
				if j == 0:
					cur[j] = pre[j] if obstacleGrid[i][0] != 1 else 0
				else:
					if obstacleGrid[i][j] == 1:
						cur[j] = 0
					else:
						if pre[j] == 0 or cur[j - 1] == 0:
							cur[j] = pre[j] if cur[j - 1] == 0 else cur[j - 1]
						else:
							cur[j] = pre[j] + cur[j - 1]
			pre = cur
		return pre[-1]
