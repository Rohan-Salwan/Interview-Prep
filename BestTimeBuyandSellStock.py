class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total=0
        i=0
        j=1
        summ=0
        while j<len(prices):
            if prices[i] < prices[j]:
                summ=prices[j]-prices[i]
                total=max(summ,total)
                j+=1
            else:
                i=j
                j+=1
        return total
                