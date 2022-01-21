class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        a=[[root]]
        b=[]
        while a!=[[]]:
            q=[]
            cur=a.pop(0)
            ans=[]
            for x in cur:
                if x:
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
                    ans.append(x.val)
                else:
                    return b
                    break
            a.append(q)
            b.append(ans)
        return b