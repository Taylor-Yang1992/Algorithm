class Solution:
    
    def deleteDuplicates(self,head):
        if not head:
            return head
        node = head
        p = head.next
        while p:
            if p.val != node.val:
                node.next = p
                node = p
            p = p.next
        node.next = None
        return head
