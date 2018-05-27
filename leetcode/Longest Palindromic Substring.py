
class Solution:
	def centerFind(self,s,i,j,l):
		while i >= 0 and j <= len(s) - 1:
			if s[i] == s[j]:
				i -= 1
				j += 1
			else:
				break
		if j - i - 1 > l[1]:
			l[1] = j - i - 1
			l[0] = s[i + 1:j]

	def longestPalindrome(self,s):
		l = ["",0]
		for (i,c) in enumerate(s):
			self.centerFind(s,i - 1,i + 1,l)
			if (i < len(s) - 1) and s[i] == s[i + 1]:
				self.centerFind(s,i - 1,i + 2,l)
		return l[0]
