class Solution:

	def canJump(self,nums):
		if len(nums) <= 1:
			return True
		cur = 1
		pos = nums[0]
		while pos < len(nums) - 1:
			t = 0
			for i in range(cur,pos + 1):
				t = max(t,i + nums[i])
			if t <= pos:
				return False
			cur = pos + 1
			pos = t
		return True
