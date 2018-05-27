
class Solution:
	def isPalindrome(self,x):
		if x == 0:
			return True
		elif x < 0 or x% 10 == 0:
			return False
		t = 0
		while t <= x:
			if t == x or t == int(x / 10):
				return True
			mode = x % 10
			t = t * 10 + mode
			x = int(x / 10)
		return False
