class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:     
        for d in nums2:
            i=0
            while i<len(nums1):
                if d==nums1[i] or d<nums1[i]:
                    nums1.insert(i,d)
                    nums1.pop()
                    m+=1
                    break
                elif i>m-1: 
                    if d > nums1[i] and nums1[i]==0:
                        nums1[i]=d
                        m+=1
                        i+=1
                        break
                else:
                    i+=1
        return nums1