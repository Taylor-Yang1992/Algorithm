class Solution:
    
    def findMin(self,nums):
        if len(nums) <= 1:
            return -1 if len(nums) == 0 else nums[0]
        v = nums[0]
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] <= nums[j]:
                v = min(v,nums[i])
                break
            else:
                mid = int((i + j) / 2)
                v = min(v,nums[mid])
                if nums[mid] >= nums[i]:
                    i = mid + 1
                else:
                    j = mid - 1
        return v
