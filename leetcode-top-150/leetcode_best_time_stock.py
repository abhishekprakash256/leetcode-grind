"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell 
that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""

"""
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""

"""
approach -- 
brute force 

#base case 
if len(nums) == 1 :
	return 0

use two pinter 
l , r = 0, r 

max_val = 0 

while r < len(nums):

	val = nums[l] - nums[r]

	if val < 0 :
		i += 1
	max_val = max(val,max_val)

	r += 1

return max_val


"""

class Solution:
	def maxProfit(self, prices) -> int:
		"""
		The function to find the max profit 
		passes leet code 
		"""

		#base case 
		if len(prices) == 1:
			return 0 
		
		#vars initilization
		l , max_val , r = 0, 0 , 1

		#loop over 
		while r < len(prices):
			
			val = prices[r] - prices[l]

			if val < 0:
				l = r
			
			r += 1
			
			max_val = max(val, max_val)
		
		return max_val




