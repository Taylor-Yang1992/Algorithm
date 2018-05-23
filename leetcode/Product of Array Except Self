class Solution:
    
    def productExceptSelf(self,nums):
        l = [1] * len(nums)
        s = 1
        for i in range(len(nums) - 1):
            l[i] = s
            s *= nums[i]
        l[-1] = s
        s = nums[-1]
        for i in range(len(nums) - 2,0,-1):
            l[i] = l[i - 1] * nums[i - 1] * s
            s *= nums[i]
        l[0] = s
        return l
