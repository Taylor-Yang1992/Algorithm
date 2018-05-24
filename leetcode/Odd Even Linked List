class Solution:
    
    def oddEvenList(self,head):
        if not head or not head.next:
            return head
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        t = 0
        while head:
            q = head.next
            if t == 0:
                p1.next = head
                p1 = head
            else:
                p2.next = head
                p2 = head
            head = q
            t = 1 - t
        p1.next = dummy2.next
        p2.next = None
        return dummy1.next
