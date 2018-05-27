class Solution:
    
    def hIndex(self,nums):
        if not nums:
            return 0
        nums.sort()
        t = 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = int((i + j) / 2)
            if nums[mid] <= len(nums) - mid:
                t = max(t,nums[mid])
                i = mid + 1
            else:
                t = max(t,len(nums) - mid)
                j = mid - 1
        return t 
