class Solution:
    
    def containsDuplicate(self,nums):
        if len(nums) <= 1:
            return False
        d = {}
        for e in nums:
            if not e in d:
                d[e] = 1
            else:
                return True
        return False
