class Solution:
    
    def minSubArrayLen(self,s,nums):
        if not nums:
            return 0
        t = len(nums) + 1
        i = 0
        v = 0
        for j in range(len(nums)):
            v += nums[j]
            if v >= s:
                while v >= s:
                    v -= nums[i]
                    i += 1
                t = min(t,j - i + 2)
        return t if t < len(nums) + 1 else 0
