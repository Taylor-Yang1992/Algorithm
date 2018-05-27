class Solution:
    
    def removeDuplicates(self,nums):
        if len(nums) <= 2:
            return len(nums)
        i = 0
        j = 1
        twiced = False
        while j <= len(nums) - 1:
            if nums[j] != nums[i] or not twiced:
                twiced = False if nums[j] != nums[i] else True
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

"""
another solution is that comparing the (i+2)th value between the (i)th value and (i+1)th value as the follows:
if nums[i + 2] == nums[i + 1] and nums[i + 2] == nums[i]:
    nums.pop(i + 2)
"""
