
class Solution:
	def lengthOfLongestSubstring(self,s):
		l = []
		mLen = 0
		for c in s:
			if not c in l:
				l.append(c)
			else:
				mLen = max(mLen,len(l))
				while c in l:
					l.pop(0)
				l.append(c)
		mLen = max(mLen,len(l))
		return mLen
