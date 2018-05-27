class Solution:

	def multiply(self,num1,num2):
		if num1 == "0" or num2 == "0":
			return "0"
		l1 = [int(num1[i]) for i in range(len(num1) - 1,-1,-1)]
		l2 = [int(num2[i]) for i in range(len(num2) - 1,-1,-1)]
		l = [0] * (len(l1) + len(l2))
		for i in range(len(l1)):
			flag = 0
			for j in range(len(l2)):
				v = l[i + j] + l1[i] * l2[j] + flag
				flag = int(v / 10)
				v = v % 10
				l[i + j] = v
			l[i + j + 1] += flag
		if l[-1] == 0:
			l.pop(-1)
		return ("".join(map(str,l)))[::-1]
