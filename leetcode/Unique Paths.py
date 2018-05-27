class Solution:

	def uniquePaths(self,m,n):
		if m == 1 or n == 1:
			return 1
		pre = [1] * n
		pre[0] = 0
		for _ in range(m - 1):
			cur = [0] * n
			for i in range(n):
				cur[i] = 1 if i == 0 else cur[i - 1] + pre[i]
			pre = cur
		return pre[-1]
