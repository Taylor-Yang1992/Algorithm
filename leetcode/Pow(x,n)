class Solution:

	def myPow(self,x,n):
		if x == 0 or n == 0:
			return 1
		sign = True
		if n < 0:
			n = -n
			sign = not sign
		val = self._myPow(x,n)
		return val if sign else 1 / val

	def _myPow(self,x,n):
		if n == 0:
			return 1
		elif n == 1:
			return x
		else:
			t = self._myPow(x,int(n / 2))
			v = t * t
			return v if n % 2 == 0 else v * x
