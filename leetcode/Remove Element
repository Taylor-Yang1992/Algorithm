class Solution:
    def removeElement(self,nums,val):
        cur = -1
        for i in range(len(nums)):
            if nums[i] != val:
                cur += 1
                nums[cur] = nums[i]
        return cur + 1
