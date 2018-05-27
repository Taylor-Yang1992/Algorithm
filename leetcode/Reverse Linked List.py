class Solution:
    
    def reverseList(self,head):
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        while head:
            p = head.next
            head.next = dummy.next
            dummy.next = head
            head = p
        return dummy.next
