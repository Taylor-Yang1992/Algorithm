class Solution:
    
    def hasPathSum(self,root,sum):
        if not root:
            return False
        s = [(root,0)]
        while s:
            e = s.pop(0)
            if e[0].val + e[1] == sum:
                if not e[0].left and not e[0].right:
                    return True
            if e[0].left:
                s.append((e[0].left,e[1] + e[0].val))
            if e[0].right:
                s.append((e[0].right,e[1] + e[0].val))
        return False
