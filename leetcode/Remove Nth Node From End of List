class Solution:
    def removeNthFromEnd(self,head,n):
        if not head:
            return head
        node = ListNode(-1)
        node.next = head
        p = node
        q = node
        skipped = 0
        while p and skipped < n:
            skipped += 1
            p = p.next
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return node.next
