class Solution:
    
    def binaryTreePaths(self,root):
        if not root:
            return []
        s = [(str(root.val),root)]
        l = []
        while s:
            n = len(s)
            for _ in range(n):
                t,node = s.pop(0)
                if not node.left and not node.right:
                    l.append(t)
                if node.left:
                    s.append((t + "->" + str(node.left.val),node.left))
                if node.right:
                    s.append((t + "->" + str(node.right.val),node.right))
        return l
