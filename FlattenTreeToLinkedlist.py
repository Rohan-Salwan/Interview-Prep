class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root==None:
            return
        else:
            if root.left==None:
                pass
            else:
                b=root.right
                root.right=root.left
                root.left=None
                temp=root.right
                while temp!=None:
                    bb=temp
                    temp=temp.right
                bb.right=b
            root.left=self.flatten(root.left)
            root.right=self.flatten(root.right)
            return root
            