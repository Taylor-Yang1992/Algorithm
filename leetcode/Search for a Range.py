class Solution:
    
    def search(self,nums,target):
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = int((i + j) / 2)
            if nums[mid] >= target:
                j = mid - 1
            else:
                i = mid + 1
        return i
    
    def searchRange(self,nums,target):
        if not nums:
            return [-1,-1]
        index = self.search(nums,target)
        if index == len(nums) or nums[index] != target:
            return [-1,-1]
        return [index,self.search(nums,target + 1) - 1]
