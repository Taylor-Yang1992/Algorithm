class Solution:
    
    def searchInsert(self,nums,target):
        if len(nums) == 0:
            return 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = int((i + j) / 2)
            if nums[mid] >= target:
                j = mid - 1
            else:
                i = mid + 1
        return i
