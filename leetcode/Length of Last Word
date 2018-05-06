class Solution:

	def lengthOfLastWord(self,s):
		if len(s) == 0:
			return 0
		i = len(s) - 1
		while i >= 0 and s[i] == " ":
			i -= 1
		if i < 0:
			return 0
		cur = i
		while i >= 0 and s[i] != " ":
			i -= 1
		return cur - i
