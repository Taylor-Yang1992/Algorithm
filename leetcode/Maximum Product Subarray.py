class Solution:
    
    def maxProduct(self,nums):
        if len(nums) <= 1:
            return 0 if len(nums) == 0 else nums[0]
        pMax = nums[0]
        pMin = nums[0]
        total = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > 0:
                if pMax > 0:
                    cMax = pMax * nums[i]
                    cMin = pMin if pMin > 0 else (0 if pMin == 0 else pMin * nums[i])
                else:
                    cMax = nums[i]
                    cMin = pMin * nums[i]
            elif nums[i] < 0:
                if pMax > 0:
                    cMax = nums[i] if pMin > 0 else (0 if pMin == 0 else pMin * nums[i])
                    cMin = pMax * nums[i]
                else:
                    cMax = pMin * nums[i]
                    cMin = nums[i]
            else:
                cMax = 0
                cMin = 0
            total = max(total,cMax)
            pMax,pMin = cMax,cMin
        return total
