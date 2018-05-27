class Solution:
	def countAndSay(self,n):
		if n <= 2:
			return "1" if n == 1 else "11"
		s = "11"
		for _ in range(3,n + 1):
			i = 0
			j = 0
			t = ""
			while j < len(s):
				if s[j] == s[i]:
					j += 1
				else:
					t = t + str(j - i) + s[i]
					i = j
			if i < len(s):
				t = t + str(len(s) - i) + s[i]
			s = t
		return s
