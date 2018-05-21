class Solution:
    
    def rob(self,nums):
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        pre1 = nums[0]
        cur1 = max(nums[:2])
        ne = max(pre1 + nums[2],cur1)
        pre1,cur1 = cur1,ne
        pre2 = nums[1]
        cur2 = max(nums[1:3])
        for i in range(3,len(nums)):
            if i == len(nums) - 1:
                return max(cur1,pre2 + nums[i],cur2)
            else:
                ne = max(pre1 + nums[i],cur1)
                pre1,cur1 = cur1,ne
                ne = max(pre2 + nums[i],cur2)
                pre2,cur2 = cur2,ne
"""
Notes:
  we record the results from the first element by pre1 and cur1 and record the results from the second element by pre2 and cur2. 
"""
