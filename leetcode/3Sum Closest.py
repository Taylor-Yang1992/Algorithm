class Solution:
	def threeSumClosest(self,nums,target):
		if len(nums) <= 2:
			return -1
		nums.sort()
		v = sum(nums[:3])
		for i in range(len(nums) - 2):
			if i == 0 or nums[i] != nums[i - 1]:
				j = i + 1
				k = len(nums) - 1
				while j < k:
					s = nums[i] + nums[j] + nums[k]
					if s == target:
						return target
					else:
						v = v if abs(v - target) < abs(s - target) else s
						if s > target:
							k -= 1
						else:
							j += 1
		return v
"""
Notes:
	Traceback is not acceptable because of the time complexity,so it's a better idead to use the "two pointers" which leads to a O(n2)
time complexity
"""
