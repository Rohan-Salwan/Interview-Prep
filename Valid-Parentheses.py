class Solution:
    def isValid(self, s: str) -> bool:
        d={
        "()":'',
        "{}":'',
        "[]":''}
        t=[]
        i=0
        crp=False
        re=False
        while i<len(s):
            if t==[]:
                if crp==False:
                    t.append(s[i])
                    crp=True
                    i+=1
                else:
                    t.append(s[i])
                    i+=1
            elif t[-1]+s[i] in d:
                    t.pop()
                    i+=1
                    re=True
            else:
                t.append(s[i])
                i+=1
        if t==[]:
            return True
        else:
            return False