class Solution:
    
    def deleteDuplicates(self,head):
        if not head or not head.next:
            return head
        node = ListNode(head.val - 1)
        p = node
        while head:
            cur = head
            while head.next and head.next.val == head.val:
                head = head.next
            if head == cur:
                p.next = head
                p = p.next
            head = head.next
        p.next = None
        return node.next
