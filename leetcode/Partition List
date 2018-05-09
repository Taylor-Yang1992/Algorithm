class Solution:
    def partition(self,head,x):
        if not head or not head.next:
            return head
        node1 = ListNode(-1)
        p1 = node1
        node2 = ListNode(-1)
        p2 = node2
        while head:
            if head.val < x:
                p1.next = head
                p1 = head
            else:
                p2.next = head
                p2 = head
            head = head.next
        p2.next = None
        p1.next = node2.next
        return node1.next
