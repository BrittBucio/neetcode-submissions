class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        compra = float('inf') # debe ser el lowest
        max_profit = 0

        for price in prices:
            if price < compra:
                compra = price
            elif price - compra > max_profit:
                max_profit = price - compra
        
        return max_profit