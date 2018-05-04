class Solution:
	def maxSubArray(self,nums):
		if not nums:
			return -1
		l = [0] * len(nums)
		l[0] = nums[0]
		for i in range(1,len(nums)):
			l[i] = max(nums[i],nums[i] + l[i - 1])
		return max(l)
