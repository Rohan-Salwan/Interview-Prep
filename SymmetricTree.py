class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def s(a,b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            return a.val==b.val and s(a.left,b.right) and s(a.right,b.left)
        return s(root.left,root.right)
            