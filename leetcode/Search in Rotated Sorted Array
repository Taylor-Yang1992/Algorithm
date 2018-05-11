class Solution:
    
    def search(self,nums,target):
        if not nums:
            return -1
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = int((i + j) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[i] < nums[j]:
                    i = mid + 1
                else:
                    if nums[i] > target:
                        i = mid + 1
                    else:
                        if nums[mid] >= nums[i]:
                            i = mid + 1
                        else:
                            j = mid - 1
            else:
                if nums[i] < nums[j]:
                    j = mid - 1
                else:
                    if nums[i] <= target:
                        j = mid - 1
                    else:
                        if nums[mid] >= nums[i]:
                            i = mid + 1
                        else:
                            j = mid - 1
        return -1
