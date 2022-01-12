class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:             
        if m==n:
            return head
        else:
            qq=m
            qp=n
            temp=head
            x=0
            d=0
            self.k=None
            count=1
            pop=0
            while temp!=None:
                if count+1==m:
                    d=temp
                    x=temp.next
                elif count==m:
                    x=temp
                elif count==n and temp.next==None:
                    y=Node(temp.val)
                elif count==n:
                    self.k=temp.next
                    y=Node(temp.val)
                    break
                count+=1
                temp=temp.next
            pop=self.dob(x,y,qq,qp)
            if d==0:
                return pop
            else:
                d.next=pop
                return head
        
    def dob(self,a,t,u,ub):    
        tp=0
        lo=0
        while a!=None:
            cur =Node(a.val)
            if u==ub:
                cur.next=tp
                tp=cur
                break
            elif lo==0:
                cur.next=self.k
                tp=cur
            else:
                cur.next=tp
                tp=cur
            lo+=1
            u+=1
            a=a.next
        return tp