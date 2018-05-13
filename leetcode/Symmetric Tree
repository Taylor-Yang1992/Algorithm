class Solution:
    
    def check(self,l,r):
        if not l or not r:
            return l == r
        if l.val != r.val:
            return False
        return self.check(l.left,r.right) and self.check(l.right,r.left)
    
    def isSymmetric(self,root):
        if not root:
            return True
        return self.check(root.left,root.right)
