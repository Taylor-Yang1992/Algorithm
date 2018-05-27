class Solution:
    
    def lowestCommonAncestor(self,head,p,q):
        if not head:
            return head
        if p == head or q == head:
            return head
        if p.val < head.val and q.val < head.val:
            return self.lowestCommonAncestor(head.left,p,q)
        elif p.val > head.val and q.val > head.val:
            return self.lowestCommonAncestor(head.right,p,q)
        else:
            return head
