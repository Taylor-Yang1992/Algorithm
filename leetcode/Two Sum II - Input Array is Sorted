class Solution:
    
    def twoSum(self,numbers,target):
        if len(numbers) <= 1:
            return [-1,-1]
        l = [-1,-1]
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                l[0],l[1] = i + 1,j + 1
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return l
