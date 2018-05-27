class Solution:
	def firstMissingPositive(self,nums):
		if not nums:
			return 1
		l = [0] * len(nums)
		for num in nums:
			if num > 0 and num <= len(l):
				l[num - 1] = 1
		for (i,num) in enumerate(l):
			if num == 0:
				return i + 1
		return len(l) + 1
