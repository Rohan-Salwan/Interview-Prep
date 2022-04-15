class Solution:
    def isHappy(self, n: int) -> bool:
        result=str(n)
        total=0
        while True:
            if result=="1":
                return True
            elif total>1000:
                return False
            count=0
            for digit in result:
                count+=int(digit)**2
            total+=1
            result=str(count)
        
