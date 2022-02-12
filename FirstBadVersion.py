class Solution:
    def firstBadVersion(self, n):
        i=0
        while True:
            if i+1==n:
                return n
                break
            n=n+i
            mid=n//2
            if isBadVersion(mid)==True:
                n=mid
            else:
                i=mid