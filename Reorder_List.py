class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        second=self.fast(head)
        prev=None
        while second:
            second.next,second,prev=prev,second.next,second
        first,second=head,prev
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2
        
    def fast(self,a):
        slow=fast=a
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        temp=slow.next
        slow.next=None
        return temp