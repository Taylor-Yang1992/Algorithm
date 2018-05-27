class Solution:
    
    def reorderList(self,head):
        if not head or not head.next:
            return
        l = []
        p = head
        while p:
            l.append(p)
            p = p.next
        node = ListNode(-1)
        p = node
        while len(l) >= 2:
            e1 = l.pop(0)
            e2 = l.pop(-1)
            p.next = e1
            e1.next = e2
            p = e2
        if l:
            e = l.pop(-1)
            p.next = e
            p = e
        p.next = None
        head = node.next

"""
def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        fast = slow = head
        temp = ListNode(0)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node = slow.next
        slow.next = None
        pre = None
        while node:
            cur = node.next
            node.next = pre
            pre = node
            node = cur
        first = head
        second = pre
        while first and second:
            node = first.next
            first.next = second
            second = second.next
            first.next.next = node
            first = node
"""
"""
Note:
  The second solution uses the fast and slow pointers to find out the divided node and then performs the insert operations.
  The main idea here is to focused on the fast and slow pointers.
"""
