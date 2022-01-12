class Solution:
    op=True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return self.op
        if p ==None or q==None or p.val!=q.val:
            self.op=False
            return
        self.isSameTree(p.left,q.left)
        self.isSameTree(p.right,q.right)
        return self.op