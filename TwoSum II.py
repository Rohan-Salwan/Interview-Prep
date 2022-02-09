class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while 0<1:
            if target==numbers[i]+numbers[j]:
                return [i+1,j+1]
                break
            elif numbers[i]+numbers[j] > target:
                j-=1
            else:
                i+=1