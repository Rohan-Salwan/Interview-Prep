class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i=0
        t={}
        while i<len(nums):
            if nums[i] in t:
                t[nums[i]].append(nums[i])
            else:
                t[nums[i]]=[nums[i]]
            i+=1
        h={}
        total=0
        for e in t:
            summ=t[e]
            if len(summ)>total:
                total=len(summ)
                h[total]= e
            else:
                pass
        d=h[total]
        return d