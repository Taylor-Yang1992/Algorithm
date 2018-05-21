class Solution:
    
    def containsNearbyDuplicate(self,nums,k):
        if not nums or k == 0:
            return False
        d = {}
        for (i,e) in enumerate(nums):
            if not e in d:
                d[e] = i
            else:
                if i - d[e] <= k:
                    return True
                else:
                    d[e] = i
        return False
"""
Notes:
    Something may be strange here. If I use the hashmap it will be the O(n) time complexity with the O(n) space complexity.
However, if i use the spide window, the time complexity is just as the previous one while has a less space complexity with O(K).
The error time is limitted is throwned. The only reason I can imagine now is that time wastes in the search operation such as: e in l 
(where l is a list)
"""
