class Solution:
    
    def search(self,nums,target):
        if not nums:
            return False
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = int((i + j) / 2)
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                if nums[i] > nums[j]:
                    if nums[mid] >= nums[i]:
                        i = mid + 1
                    else:
                        if nums[j] >= target:
                            i = mid + 1
                        else:
                            j = mid - 1
                elif nums[i] == nums[j]:
                    j -= 1
                else:
                    i = mid + 1
            else:
                if nums[i] > nums[j]:
                    if nums[mid] >= nums[i]:
                        if nums[j] >= target:
                            i = mid + 1
                        else:
                            j = mid - 1
                    else:
                        j = mid - 1
                elif nums[i] == nums[j]:
                    j -= 1
                else:
                    j = mid - 1
        return False
