class Solution:
    
    def sortColors(self,nums):
        if len(nums) <= 1:
            return
        i = -1
        j = len(nums)
        k = 0
        while k < j:
            if nums[k] == 0:
                i += 1
                nums[i],nums[k] = 0,nums[i]
                k += 1
            elif nums[k] == 2:
                j -= 1
                nums[j],nums[k] = 2,nums[j]
            else:
                k += 1
