class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=len(s)-1
        i=0
        while l>=0:
            if s[l]==" " and i>0:
                return i
            elif s[l]==" ":
                pass
            else:
                i+=1
            l-=1
        return i