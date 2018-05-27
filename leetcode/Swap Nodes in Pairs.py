class Solution:
	def swap(self,head,k):
		root = ListNode(-1)
		root.next = head
		l = []
		cur = root
		while head:
			if len(l) == k:
				while l:
					node = l.pop(-1)
					cur.next = node
					cur = cur.next
			l.append(head)
			head = head.next
		right = (len(l) == k)
		while l:
			node = l.pop(-1) if right else l.pop(0)
			cur.next = node
			cur = cur.next
		cur.next = None
		return root.next

	def swapPairs(self,head):
		return self.swap(head,2)
