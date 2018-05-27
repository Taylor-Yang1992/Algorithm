class Solution:
    
    def check(self,root,l,r):
        if not root:
            return True
        if l == "N":
            if r != "N" and root.val > r:
                return False
        elif r == "N":
            if root.val < l:
                return False
        else:
            if root.val < l or root.val > r:
                return False
        return self.check(root.left,l,root.val - 1) and self.check(root.right,root.val + 1,r)
    
    def isValidBST(self,root):
        return self.check(root,"N","N")
