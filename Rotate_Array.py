class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            k = k % len(nums)
        ans = nums[-k :] + nums[: -k]
        nums[:] = ans[:]