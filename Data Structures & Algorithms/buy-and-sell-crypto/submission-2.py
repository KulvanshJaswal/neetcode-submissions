class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most = 0
        minimum = prices[0]
        for i in range(1, len(prices)):
            minimum = min(minimum, prices[i])

            if prices[i] > minimum:
                most = max(most, prices[i] - minimum)
            
        return most