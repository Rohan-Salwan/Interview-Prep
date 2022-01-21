class node:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, ino: List[int], post: List[int]) -> Optional[TreeNode]:
        def build(ino):
            if ino==[]:
                return
            x=checker(ino,post)
            l=ino.index(x)
            n=node(val=x)
            ino.remove(x)
            post.remove(x)
            n.left=build(ino[:l])
            n.right=build(ino[l:])
            return n
        def checker(a,b):
            i=len(post)-1
            while i>=0:
                if b[i] in a:
                    return b[i]
                    break
                else:
                    i-=1
        return build(ino)