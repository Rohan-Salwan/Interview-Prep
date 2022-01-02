class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummyNode=ListNode(0)
        curr=dummyNode
        p,q=l1,l2
        carry=0
        while p or q:
            x,y=0,0
            if p:
                x=p.val
            if q:
                y=q.val
            sum=carry+x+y
            carry=sum//10
            curr.next=ListNode(sum%10)
            curr=curr.next
            if p:p=p.next
            if q:q=q.next
        if carry>0:
            curr.next=ListNode(carry)
        return dummyNode.next
        