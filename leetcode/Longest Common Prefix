
class Solution:
	def longestCommonPrefix(self,strs):
		if len(strs) == 0:
			return ""
		if len(strs) == 1:
			return strs[0]
		result = ""
		length = min((len(s) for s in strs))
		for i in range(length):
			if all((s.startswith(strs[0][:i + 1]) for s in strs[1:])):
				result = strs[0][:i + 1]
			else:
				break
		return result
