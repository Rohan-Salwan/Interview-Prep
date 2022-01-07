class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            a=nums.index(target)
        except:
            return [-1,-1]
        c=nums[::-1]
        b=c.index(target)
        b+=1
        b=len(nums)-b
        return [a,b]
        