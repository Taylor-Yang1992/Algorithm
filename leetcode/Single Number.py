class Solution:
    
    def singleNumber(self,nums):
        val = 0
        for c in nums:
            val = val ^ c
        return val
