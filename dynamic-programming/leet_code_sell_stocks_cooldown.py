"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

"""

prices = [1,2,3,0,2]
out = 3 


class Solution():
	def maxProfit(self,prices):
		"""
		The function to find the max profit
		"""

		dp = {}

		def dfs(i,buying):

			if i >= len(prices):
				return 0 

			if (i,buying) in dp :
				return dp[(i,buying)]

			if buying :
				buy = dfs(i +1 , not buying ) - prices[i]
				cooldown = dfs(i+1,buying)
				dp[(i,buying)] = max(buy,cooldown)

			else:
				sell = dfs(i+2,not buying) + prices[i]
				cooldown = dfs(i+1,buying)
				dp[(i,buying)] = max(sell,cooldown)


			return dp[(i,buying)]

		return dfs(0,True)



class Solution2():
    def maxProfit(self, prices: List[int]) -> int:
        sold = 0                # Represents the maximum profit if the stock is sold on the current day
        hold = float('-inf')    # Represents the maximum profit if the stock is held (bought) on the current day
        rest = 0                # Represents the maximum profit if no action is taken (rest) on the current day
        
        for price in prices:    # Iterating through each day's stock price
            prev_sold = sold    # Storing the previous value of 'sold' for updating 'rest'
            
            # Updating 'sold' with the profit from holding the stock on the previous day plus the current day's stock price
            sold = hold + price
            
            # Updating 'hold' to the maximum of its current value and the profit from resting on the previous day minus the current day's stock price
            hold = max(hold, rest - price)
            
            # Updating 'rest' to the maximum of its current value and the profit from selling the stock on the previous day
            rest = max(rest, prev_sold)
        
        # Returning the maximum profit achievable, which is the maximum between 'sold' and 'rest'
        return max(sold, rest)

