class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t={}
        temp=head
        prev=None
        while temp!=None:
            if temp.val in t:
                prev.next=temp.next
            else:
                t[temp.val]=True
                prev=temp
            temp=temp.next
        return head