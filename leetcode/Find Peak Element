class Solution:
    
    def check(self,nums,i,j):
        if i <= j:
            mid = int((i + j) / 2)
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            x = self.check(nums,i,mid - 1)
            if x != -1:
                return x
            else:
                return self.check(nums,mid + 1,j)
        return -1
    
    def findPeakElement(self,nums):
        if len(nums) <= 1:
            return 0 if len(nums) == 1 else -1
        nums.insert(0,nums[0] - 1)
        nums.append(nums[-1] - 1)
        t = self.check(nums,1,len(nums) - 2)
        return t - 1 if t != -1 else t
"""
Notes:
    Something is out of consideration because the num[-1] and nums[n] are alway -max, so it means there always be at least one peak.
"""
