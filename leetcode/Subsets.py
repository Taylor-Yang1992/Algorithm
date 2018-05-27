class Solution:
    
    def subsets(self,nums):
        if len(nums) <= 1:
            return [[]] if len(nums) == 0 else [[],[nums[0]]]
        pre = [[],[nums[0]]]
        for i in range(1,len(nums)):
            cur = []
            for e in pre:
                cur.append(e)
                cur.append(e + [nums[i]])
            pre = cur
        return pre   
