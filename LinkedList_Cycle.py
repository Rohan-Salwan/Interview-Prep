class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        t={}
        temp=head
        lim=False
        while temp!=None:
            if temp in t:
                lim=True
                return lim
            else:
                t[temp]=True
            temp=temp.next
        return lim