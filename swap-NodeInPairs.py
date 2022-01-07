class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp=head
        if head==None:
            return head
        elif head.next==None:
            return head
        while temp!=None and temp.next!=None:
            c=temp.next.val
            temp.next.val=temp.val
            temp.val=c
            temp=temp.next.next
        return head