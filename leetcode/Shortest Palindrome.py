class Solution:
    
    def shortestPalindrome(self,s):
        if not s:
            return s
        v = s[0]
        for i in range(1,len(s)):
            if s[:i + 1] == s[:i + 1][::-1]:
                v = s[:i + 1]
            else:
                v = s[i] + v + s[i]
        return v
"""
Notes:
  The best solution is to use the KMP algorithm which time complexity is O(n).
"""
