class Solution:
    
    def rightSideView(self,root):
        if not root:
            return []
        l = []
        s = [root]
        while s:
            n = len(s)
            for i in range(n):
                x = s.pop(0)
                if i == n - 1:
                    l.append(x.val)
                if x.left:
                    s.append(x.left)
                if x.right:
                    s.append(x.right)
        return l
