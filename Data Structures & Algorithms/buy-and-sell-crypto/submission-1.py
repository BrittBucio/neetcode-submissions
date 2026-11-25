class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = prices[left] - prices[right]
        # maxProfit = max(profit, maxProfit)
        # como actualizamos profit? 
        min_price = prices[0]
        max_profit = 0
        

        for price in prices:
            # 1. ¿El precio actual es menor que mi mínimo histórico?
            if price < min_price:
                min_price = price
            # 2. ¿Cuánto ganaría si vendiera hoy?
            profit = price - min_price
            # 3. ¿Es esa ganancia mejor que mi máximo histórico?
            max_profit = max(profit, max_profit)



        return max_profit
