class Solution:
    def climbStairs(self, n: int) -> int:
        if 1==n:
            return n
        f0,f1=1,1
        ans=0  
        for i in range(2,n+1):
            ans=f0+f1
            f0=f1
            f1=ans
        return ans