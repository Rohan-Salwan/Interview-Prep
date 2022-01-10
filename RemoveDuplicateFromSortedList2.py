class node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        array={}
        if head is None:
            return head
        cur=node(val=0)
        temp=cur
        while head.next!=None:
            if head.val==head.next.val:
                array[head.val]=True
            if head.val not in array:
                temp.next=node(val=head.val)
                temp=temp.next
            head=head.next
        if head.val not in array:
            temp.next=node(val=head.val)
            temp=temp.next
        return cur.next