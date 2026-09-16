class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0 , 1
        max_prof = 0
        while end < len(prices):
            buy, sell = prices[start], prices[end]
            profit = sell - buy
            if profit > max_prof:
                max_prof = profit
            if sell < buy:
                start = end

            end += 1

        return max_prof
            
                



