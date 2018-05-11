class Solution:
    
    def fourSum(self, nums, target):
        if len(nums) < 3:
            return []
        nums.sort()
        l = []
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1,len(nums) - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        m = j + 1
                        n = len(nums) - 1
                        v = target - nums[i] - nums[j]
                        while m < n:
                            if nums[m] + nums[n] == v:
                                if not [nums[i],nums[j],nums[m],nums[n]] in l:
                                    l.append([nums[i],nums[j],nums[m],nums[n]])
                                while m < n and nums[m] == nums[m + 1]:
                                    m += 1
                                m += 1
                                while n > m and nums[n] == nums[n - 1]:
                                    n -= 1
                                n -= 1 
                            elif nums[m] + nums[n] < v:
                                while m < n and nums[m] == nums[m + 1]:
                                    m += 1
                                m += 1
                            else:
                                while n > m and nums[n] == nums[n - 1]:
                                    n -= 1
                                n -= 1
        return l
