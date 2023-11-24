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
out2 = 25


stock_lst3 = [1,2,4,2,1]
out3 = 3

stock_lst4 = [2]
out4 = 4 


#the soln 


class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""

		