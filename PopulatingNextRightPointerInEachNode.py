class Solution:
    def connect(self, root: 'Node') -> 'Node':
        array=[[root]]
        de=root
        while True:
            if array==[[]]:
                return root
                break
            re=array.pop(0)
            bro=[]
            for e in re:
                if e:
                    if e.left:
                        bro.append(e.left)
                    if e.right:
                        bro.append(e.right)
            array.append(bro)
            i=0
            while i<len(bro):
                if i+1==len(bro):
                    bro[i].next=None
                    break
                if bro[i]:
                    bro[i].next=bro[i+1]
                i+=1
                