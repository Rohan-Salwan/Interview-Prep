class Solution:
    def isPalindrome(self, head) -> bool:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        if arr==arr[::-1]:
            return True