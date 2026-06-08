class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        for i in range(len(prices)-1):
            maxP=0
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    maxP = max(maxP, (prices[j]-prices[i]))
            result=max(result, maxP)
        return result
