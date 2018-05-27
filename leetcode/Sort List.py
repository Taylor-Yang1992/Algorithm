class Solution:
    
    def mergeSort(self,head,num):
        if num == 1:
            return head
        k = 1
        p = head
        while k < int(num / 2):
            k += 1
            p = p.next
        q = p
        p = p.next
        q.next = None
        head1 = self.mergeSort(head,k)
        head2 = self.mergeSort(p,num - k)
        dummy = ListNode(-1)
        r = dummy
        while head1 and head2:
            if head1.val < head2.val:
                r.next = head1
                head1 = head1.next
                r = r.next
            else:
                r.next = head2
                head2 = head2.next
                r = r.next
        if head1:
            r.next = head1
        if head2:
            r.next = head2
        return dummy.next
    
    def sortList(self,head):
        if not head or not head.next:
            return head
        num = 0
        p = head
        while p:
            num += 1
            p = p.next
        return self.mergeSort(head,num)
