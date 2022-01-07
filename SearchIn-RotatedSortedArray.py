class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            ind=nums.index(target)
            return ind
        except:
            return -1