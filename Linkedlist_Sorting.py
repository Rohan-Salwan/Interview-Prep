class node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        mid=self.divide(head)
        jbl=mid.next
        mid.next=None
        l1=self.sortList(head)
        l2=self.sortList(jbl)
        blo=self.mergelist(l1,l2)
        return blo
    def divide(self,a):
        slow=a
        fast=a.next
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergelist(self,aa,bb):
        tt=node(0)
        ab=tt
        while aa!=None and bb!=None: 
            if aa.val <= bb.val:
                tt.next=aa
                tt=tt.next
                aa=aa.next
            else:
                tt.next=bb
                tt=tt.next
                bb=bb.next
        while aa!=None:
            tt.next=aa
            tt=tt.next
            aa=aa.next
        while bb!=None:
            tt.next=bb
            tt=tt.next
            bb=bb.next
        return ab.next