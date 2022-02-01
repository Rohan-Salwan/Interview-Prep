class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        actual=""
        for e in s:
            if e.isalnum():
                actual+=e
        bro=actual[::-1]
        if bro==actual:
            return True
        else:
            return False