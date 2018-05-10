class Solution:
    
    def subsetsWithDup(self,nums):
        if len(nums) <= 1:
            return [[]] if not nums else [[],[nums[0]]]
        nums.sort()
        pre = [[],[nums[0]]]
        for i in range(1,len(nums)):
            cur = [e for e in pre]
            if nums[i] != nums[i - 1]:
                for e in pre:
                    cur.append(e + [nums[i]])
            else:
                for e in pre:
                    l = e + [nums[i]]
                    if not l in cur:
                        cur.append(l)
            pre = cur
        return pre
