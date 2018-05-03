class Solution:
	def mergeTwoLists(self,l1,l2):
		if not l1:
			return l2
		if not l2:
			return l1
		root = ListNode(-1)
		cur = root
		while l1 and l2:
			if l1.val < l2.val:
				cur.next = l1
				cur = l1
				l1 = l1.next
			else:
				cur.next = l2
				cur = l2
				l2 = l2.next
		if l1:
			cur.next = l1
		if l2:
			cur.next = l2
		return root.next
