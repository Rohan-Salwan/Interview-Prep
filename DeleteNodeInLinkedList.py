class Solution:
    def deleteNode(self, node):
        temp=node
        while temp.next!=None:
            temp.val=temp.next.val
            a=temp
            temp=temp.next
        a.next=None