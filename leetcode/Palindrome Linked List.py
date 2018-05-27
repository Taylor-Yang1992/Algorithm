class Solution:
    
    def isPalindrome(self,head):
        if not head or not head.next:
            return True
        slow = head
        fast = head
        t = 0
        while fast and fast.next:
            t += 1
            slow = slow.next
            fast = fast.next.next
        n = None
        while slow:
            p = slow.next
            slow.next = n
            n = slow
            slow = p
        for _ in range(t):
            if head.val != n.val:
                return False
            head = head.next
            n = n.next
        return True
"""
Notes:
Fortunately I used the fast and slow pointers to work out this problem.
"""
