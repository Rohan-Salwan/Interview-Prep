class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        t={}
        temp=head
        ap=0
        j=0
        while temp!=None:
            if temp in t:
                return t[temp]
            else: 
                t[temp]=temp
            ap+=1
            temp=temp.next
        return None