class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        d={}
        while i<len(nums):
            if nums[i] in d:
                nums.remove(nums[i])
                i-=1
            else:
                d[nums[i]]=True
            i+=1