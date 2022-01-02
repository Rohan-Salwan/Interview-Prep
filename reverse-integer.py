class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        t=x[0]
        a=0
        try:
            int(t)*0==0
            x=x[::-1]
            x=int(x)
            a = x
        except: 
            a=x[1:]
            a=a[::-1]
            j=x[0]
            j+=a
            ab=int(j)
            a=ab
        if a > 2147483647:
            return 0
        elif a < -2147483648:
            return 0
        else:
            return a
        