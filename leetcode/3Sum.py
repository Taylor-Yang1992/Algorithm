class Solution:
    def threeSum(self,nums):
        if len(nums) <= 2:
            return []
        nums = sorted(nums)
        l = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if nums[j] + nums[k] == -nums[i]:
                        l.append([nums[i],nums[j],nums[k]])
                        j += 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        k -= 1
                        while k > j and nums[k] == nums[k + 1]:
                            k -= 1
                    elif nums[j] + nums[k] < -nums[i]:
                        j += 1
                    else:
                        k -= 1
        return l
