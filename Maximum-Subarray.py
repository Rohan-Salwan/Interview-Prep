class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ab=nums[0]
        total=0
        for e in nums:
            if total < 0:
                total=0
            total+=e
            ab=max(total,ab)
        return ab