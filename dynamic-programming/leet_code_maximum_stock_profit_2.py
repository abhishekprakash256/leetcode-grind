"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

"""
Input: prices = [7,1,5,3,6,4,0]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.



Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""



"""


[2,1,2,1,0,1,2]


appoach -- 

1. 
track the sell of the max value

two pointer 

move till left is small than right 

if left val is small than right then calc the stock value

keep track and then give max value at the end 

"""



class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		accepted in leetcode but slow
		"""

		#base case 
		if len(prices) == 1:
			return 0

		l , r = 0 , 1

		length = len(prices)
		max_profit = 0 


		while r < length:

			if prices[l] > prices[r]:
				l = r
				r +=1

			else:
				curr_profit = prices[r] - prices[l]
				max_profit = max(curr_profit,max_profit)
				r +=1

		return max_profit




















