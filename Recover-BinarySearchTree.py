class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def traversal(node):
            if node==None:
                return
            traversal(node.left)
            arr.append(node)
            traversal(node.right)
        arr=[]
        traversal(root)
        i=x=y=0
        while i<len(arr):
            if arr[i].val>arr[i+1].val:
                x=i
                y=len(arr)-1
                while y>=0:
                    if arr[x].val>arr[y].val:
                        temp=arr[x].val
                        arr[x].val=arr[y].val
                        arr[y].val=temp
                        break
                    y-=1
                break
            i+=1