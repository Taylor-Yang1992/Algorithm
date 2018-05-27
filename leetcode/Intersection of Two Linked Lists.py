class Solution:
    
    def getIntersectionNode(self,headA,headB):
        if not headA or not headB:
            return None
        l1 = 0
        p = headA
        while p:
            l1 += 1
            p = p.next
        l2 = 0
        p = headB
        while p:
            l2 += 1
            p = p.next
        p = headA
        q = headB
        while l1 != l2:
            if l1 < l2:
                q = q.next
                l2 -= 1
            else:
                p = p.next
                l1 -= 1
        while p != q:
            p = p.next
            q = q.next
        return p
