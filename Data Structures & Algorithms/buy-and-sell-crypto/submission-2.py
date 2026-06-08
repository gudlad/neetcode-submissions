class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprcsn = prices[0]
        maxP = 0
        for j in range(len(prices)):
            minprcsn = min(minprcsn, prices[j])
            maxP = max(maxP, prices[j]-minprcsn)
        return maxP