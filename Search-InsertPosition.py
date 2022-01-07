class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0]==target:
            return 0
        if nums[-1]<target:
            return len(nums)
        if nums[0]>target:
            return 0
        i=0
        j=len(nums)-1
        old=0
        while True:
            mid=(i+j)//2
            if old==mid:
                return old+1
            old=mid
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                j=mid
            else:
                i=mid