class Solution:
	def addTwoNumbers(self,l1,l2):
		head = ListNode(-1)
		p = head
		flag = 0
		while l1 or l2:
			val = flag
			if l1:
				val += l1.val
				l1 = l1.next
			if l2:
				val += l2.val
				l2 = l2.next
			flag = int(val / 10)
			val = val % 10
			p.next = ListNode(val)
			p = p.next
		if flag:
			p.next = ListNode(flag)
		return head.next
