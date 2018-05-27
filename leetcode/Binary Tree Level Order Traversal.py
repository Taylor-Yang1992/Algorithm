class Solution:
    
    def levelOrder(self,root):
        if not root:
            return []
        r = []
        s = [root]
        while s:
            n = len(s)
            t = []
            for i in range(n):
                e = s.pop(0)
                t.append(e.val)
                if e.left:
                    s.append(e.left)
                if e.right:
                    s.append(e.right)
            r.append(t)
        return r
