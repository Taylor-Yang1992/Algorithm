class Solution:
    
    def dfs(self,root,l):
        if root:
            self.dfs(root.left,l)
            l.append(root.val)
            self.dfs(root.right,l)
    
    def inorderTraversal(self,root):
        l = []
        self.dfs(root,l)
        return l
