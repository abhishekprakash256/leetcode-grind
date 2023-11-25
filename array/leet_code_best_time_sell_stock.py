"""

best time to sell stock and buy it \
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""



#test cases 
stock_lst = [1,2,3,4,5]
out = 4

stock_lst2 = [1,2,5,2,1,23,4,6] 
out2 = 28


stock_lst3 = [1,2,4,2,1]
out3 = 3

stock_lst4 = [2]
out4 = 4 


#the soln 


"""
1,2,3,4,5,6


"""

class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""

		left = 0 
		right = left + 1

		if len(prices) == 1 or len(prices) == 0:
			return 0 

		#strat the loop 

		profit = 0 

		for i in range(1,len(prices)):

			if prices[i] > prices[i-1]:

				profit += (prices[i] - prices[i-1])

		return profit




if __name__ == "__main__":

	sol = Solution()

	res = sol.maxProfit(stock_lst2)

	print(res)
