class Solution:

	def jump(self,nums):
		if len(nums) <= 1:
			return 0
		times = 1
		cur = 1
		pos = nums[0]
		while pos < len(nums) - 1:
			times += 1
			t = 0
			for i in range(cur,pos + 1):
				t = max(t,i + nums[i])
			cur = pos
			pos = t
		return times
