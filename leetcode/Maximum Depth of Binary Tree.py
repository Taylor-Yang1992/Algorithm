class Solution:
    
    def maxDepth(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif not root.left or not root.right:
            return 1 + self.maxDepth(root.left) if not root.right else 1 + self.maxDepth(root.right)
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
