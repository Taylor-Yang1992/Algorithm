
class Solution:
	def convert(self,s,numRows):
		if numRows == 1:
			return s
		l = [[] for i in range(numRows)]
		i = -1
		mode = 1
		for c in s:
			i += mode
			l[i].append(c)
			if i == 0:
				mode = 1
			elif i == numRows - 1:
				mode = -1
		result = ["".join(l[i]) for i in range(numRows)]
		return "".join(result)
