class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=1
        re=10000
        nums.append(0)
        while i<len(nums):
            if sum(nums[i:j])>=target:
                if re>(j-i):
                    re=(j-i)
                i+=1
                continue
            if j+1!=len(nums):
                j+=1
            else:
                i+=1
        if re==10000:
            return 0
        return re
