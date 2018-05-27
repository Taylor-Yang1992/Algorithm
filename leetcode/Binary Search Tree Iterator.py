class Solution:
    
    def __init__(self,root):
        self.l = []
        p = root
        while p:
            self.l.append(p)
            p = p.left
    
    def hasNext(self):
        return not (not self.l)
    
    def next(self):
        x = self.l.pop(-1)
        t = x.val
        y = x.right
        while y:
            self.l.append(y)
            y = y.left
        return t
