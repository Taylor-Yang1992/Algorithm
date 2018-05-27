class Solution:
    
    def sumNumbers(self,root):
        if not root:
            return 0
        total = 0
        l = [(root,0)]
        while l:
            e,s = l.pop(0)
            if not e.left and not e.right:
                total += s * 10 + e.val
            if e.left:
                l.append((e.left,s * 10 + e.val))
            if e.right:
                l.append((e.right,s * 10 + e.val))
        return total
