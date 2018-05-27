class Solution:
    
    def insertionSortList(self,head):
        if not head or not head.next:
            return head
        p = head.next
        q = head
        while p:
            if p.val >= q.val:
               q.next = p
               q = p
               p = p.next
            else:
                t = p.next
                if p.val <= head.val:  
                    p.next = head
                    head = p
                else:
                    r = head
                    while r.next.val < p.val:
                        r = r.next
                    p.next = r.next
                    r.next = p
                p = t    
        q.next = None
        return head
