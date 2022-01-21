class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        re=[[root.val]]
        q=[[root]]
        tom=False
        while q:
            l=q.pop(0)
            arr=[]
            tt=[]
            for e in l:
                if e.left:
                    arr.append(e.left.val)
                    tt.append(e.left)
                if e.right:
                    arr.append(e.right.val)
                    tt.append(e.right)
            if tt==[]:
                break
            if tom==False:
                arr=arr[::-1]
                tom=True
            else:
                tom=False
            q.append(tt)
            re.append(arr)
        return re