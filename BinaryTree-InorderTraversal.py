class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        t=[]
        e=[]
        cur=root
        while 0<1:
            if cur!=None:
                while cur!=None:
                    e.append(cur)
                    cur=cur.left
            elif e!=[]:
                cur=e.pop()
                t.append(cur.val)
                cur=cur.right
            else:
                break
        return t
            