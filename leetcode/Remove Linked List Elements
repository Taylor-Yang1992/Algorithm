class Solution:
    
    def removeElements(self,head,val):
        if not head:
            return head
        node = ListNode(val - 1)
        p = node
        while head:
            if head.val != val:
                p.next = head
                p = head
            head = head.next
        p.next = None
        return node.next
