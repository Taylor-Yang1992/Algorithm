class Solution:
    
    def reverseBetween(self,head,m,n):
        node = ListNode(-1)
        node.next = head
        p = node
        count = 0
        while count < m - 1:
            count += 1
            p = p.next
        p1 = p
        p2 = p.next
        q = p2
        p1.next = None
        for i in range(m,n + 1):
            p = q
            q = q.next
            p.next = p1.next
            p1.next = p
        p2.next = q
        return node.next
