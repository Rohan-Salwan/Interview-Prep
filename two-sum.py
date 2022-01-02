class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<=1:
            return False
        ab={}
        for i in range(len(nums)):
            if nums[i] in ab:
                return [ab[nums[i]],i]
            else:
                ab[target-nums[i]]=i