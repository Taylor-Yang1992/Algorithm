class Solution(object):
    def deleteNode(self,node):
        p = node
        q = node.next
        while q.next:
            p.val = q.val
            p = q
            q = q.next
        p.val = q.val
        p.next = None
