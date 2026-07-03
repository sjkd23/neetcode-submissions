class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        cheapest = prices[0]
        for i in prices:
            if cheapest > i:
                cheapest = i
            else:
                if profit < i - cheapest:
                    profit = i - cheapest 
            
        return profit
