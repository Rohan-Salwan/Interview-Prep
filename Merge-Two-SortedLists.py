class ListNode:
     def __init__(self, val=0):
        self.val = val
        self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None and l2!=None:
            return l2
        if l1!=None and l2==None:
            return l1
        ch=ListNode(0)
        head=ch
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                ch.next=l1
                l1=l1.next
            else:
                ch.next=l2
                l2=l2.next
            ch=ch.next
            if l1!=None:
                ch.next=l1
            else:
                ch.next=l2
        return head.next
                