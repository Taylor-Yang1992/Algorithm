class Solution:
    
    def moveZeroes(self,nums):
        if len(nums) <= 1:
            return
        i = 0
        j = 0
        while j <= len(nums) - 1:
            if nums[j] != 0:
                if i != j:
                    nums[i] = nums[j]
                    nums[j] = 0
                i += 1
            j += 1
