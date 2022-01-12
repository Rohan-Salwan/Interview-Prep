class Solution:
    val=-(2**99)
    tom=True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.traversal(root)
        return self.tom
        
        
    def traversal(self,root):
        if root==None:
            return
        self.traversal(root.left)
        if self.val<root.val:
            self.val=root.val
        else:
            self.tom=False
        self.traversal(root.right)