class Solution:
    
    def flat(self,root):
        if not root.left and not root.right:
            return (root,root)
        if not root.left:
            (head,tail) = self.flat(root.right)
            root.right = head
            return (root,tail)
        elif not root.right:
            (head,tail) = self.flat(root.left)
            root.left = None
            root.right = head
            return (root,tail)
        else:
            (head1,tail1) = self.flat(root.left)
            (head2,tail2) = self.flat(root.right)
            root.left = None
            root.right = head1
            tail1.right = head2
            return (root,tail2)
    
    def flatten(self,root):
        if not root:
            return
        self.flat(root)
