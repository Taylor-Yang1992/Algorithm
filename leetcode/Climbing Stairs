class Solution:

	def climbStairs(self,n):
		if n <= 2:
			return n
		else:
			f1 = 1
			f2 = 2
			for i in range(3,n + 1):
				f = f1 + f2
				f1,f2 = f2,f
			return f2
