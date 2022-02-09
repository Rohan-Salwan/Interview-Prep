class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:
            return
        head.next=self.removeElements(head.next,val)
        if head.val==val:
            temp=head.next
        else:
            temp=head
        return temp