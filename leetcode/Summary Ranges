class Solution:
    
    def summaryRanges(self,nums):
        if not nums:
            return []
        l = []
        i = 0
        while i < len(nums):
            j = i
            while i + 1 < len(nums) and nums[i + 1] - nums[i] == 1:
                i += 1
            l.append(str(nums[j]) + "->" + str(nums[i]) if i != j else str(nums[j]))
            i += 1
        return l
