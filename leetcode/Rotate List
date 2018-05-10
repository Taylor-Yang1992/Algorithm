
class Solution:
    
    def rotateRight(self,head,k):
        if not head or not head.next:
            return head
        l = 0
        p = head
        while p:
            l += 1
            if not p.next:
                tail = p
            p = p.next
        k = k % l
        if k == 0:
            return head
        skipped = 1
        p = head
        while skipped < l - k:
            p = p.next
            skipped += 1
        q = p.next
        p.next = None
        tail.next = head
        return q

"""
when calculating the length of list,record the tail node to avoid the extra operation
"""
