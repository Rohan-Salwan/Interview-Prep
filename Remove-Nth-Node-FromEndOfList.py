class Solution:
    count=0
    t=False
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head==None:
            return
        self.removeNthFromEnd(head.next,n)
        self.count+=1
        if self.count==n+1:
            self.t=True
            head.next=head.next.next
        if self.t==False:
            return head.next
        else:
            return head