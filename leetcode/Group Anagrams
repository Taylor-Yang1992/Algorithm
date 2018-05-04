class Solution:
	def groupAnagrams(self,strs):
		if not strs:
			return []
		d = {}
		for i in range(len(strs)):
			l = [c for c in strs[i]]
			l.sort()
			s = "".join(l)
			if s in d:
				d[s].append(strs[i])
			else:
				d[s] = [strs[i]]
		return list(d.values())
