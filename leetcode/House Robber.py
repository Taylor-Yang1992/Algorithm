class Solution:
    
    def rob(self,nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return nums[0] if len(nums) == 1 else max(nums)
        pre = nums[0]
        cur = max(nums[:2])
        for i in range(2,len(nums)):
            ne = max(cur,pre + nums[i])
            pre,cur = cur,ne
        return cur
