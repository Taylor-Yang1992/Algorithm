class Solution:
    
    def tb(self,root,c,s,cur,l):
        if not root.left and not root.right:
            if c + root.val == s:
                l.append(cur + [root.val])
            return
        if root.left:
            self.tb(root.left,c + root.val,s,cur + [root.val],l)
        if root.right:
            self.tb(root.right,c + root.val,s,cur + [root.val],l)
    
    def pathSum(self,root,s):
        if not root:
            return []
        l = []
        self.tb(root,0,s,[],l)
        return l
