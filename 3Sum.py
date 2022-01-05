class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums==[]:
            return nums
        if  len(nums)<3:
            return []
        job=self.sort(nums)
        l=[]
        i=0
        j=1
        k=len(job)-1
        pro={}
        while i < len(job)-1:
            if j==k:
                i+=1
                j=i+1
                k=len(job)-1
            elif job[i]+job[j]+job[k]==0:
                if l==[]:
                    l.append([job[i],job[j],job[k]])
                    pro[(job[i],job[j],job[k])]=True
                else:
                    if (job[i],job[j],job[k]) in pro:
                        pass
                    else:
                        l.append([job[i],job[j],job[k]])
                        pro[(job[i],job[j],job[k])]=True
                    if job[i]+job[j+1]+job[k]>0:
                        k-=1
                    else:
                        j+=1
            elif job[i]+job[j]+job[k]>0:
                k-=1
            else:
                j+=1
        return l
        
                
    def sort(self,a):
        if len(a)>1:
            mid = len(a)//2
            aa=a[:mid]
            bb=a[mid:]
            self.sort(aa)
            self.sort(bb)
            q=w=e=0
            while q<len(aa) and w < len(bb):
                if aa[q]<bb[w]:
                    a[e]=aa[q]
                    q+=1
                else:
                    a[e]=bb[w]
                    w+=1
                e+=1
            while q<len(aa):
                a[e]=aa[q]
                q+=1
                e+=1
            while w<len(bb):
                a[e]=bb[w]
                w+=1
                e+=1
            return a