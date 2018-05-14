class Solution:
    
    def minDepth(self,root):
        if not root:
            return 0
        if not root.left or not root.right:
            return 1 + (self.minDepth(root.left) if not root.right else self.minDepth(root.right))
        else:
            return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
