class Solution:
	def longestValidParentheses(self,s):
		if len(s) <= 1:
			return 0
		s = "#" + s
		l = [0 for c in s]
		for i in range(1,len(s)):
			if s[i] == ")":
				if s[i - 1] == "(":
					l[i] = l[i - 2] + 2
				elif s[i - l[i - 1] - 1] == "(":
					l[i] = l[i - l[i - 1] - 2] + l[i - 1] + 2
		val = 0
		for i in range(len(s) - 1,0,-1):
			if l[i] > 0:
				m = 0
				while i >= 0 and l[i] > 0:
					m += l[i]
					i = i - l[i]
				val = max(val,m)
		return val
"""
Something may be better than here.
Just use the left and right pointers scanning the "s" from left to right and from right to left
A beautiful solution!
"""
