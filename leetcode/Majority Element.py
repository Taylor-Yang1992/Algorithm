class Solution:
    
    def majorityElement(self,nums):
        if len(nums) <= 1:
            return -1 if len(nums) == 0 else nums[0]
        v = 0
        t = 0
        for e in nums:
            if t == 0:
                t += 1
                v = e
            else:
                if e == v:
                    t += 1
                else:
                    t -= 1
        return v
