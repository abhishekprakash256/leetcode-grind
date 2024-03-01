"""
the function to find the bes time to buy and sell stock 
"""

prices = [7,1,5,3,6,4]
out = 5 


prices2 = [7,6,4,3,1]
out2 = 0 


"""
basic algo -- 

uisng the n^2 iteration 


then find the max each time and update the max 





"""



class Solution():
	def maxProfit_brute_force(self,nums):
		"""
		The brute forrce approach to find max profit
		"""

		max_profit = 0 

		for i in range(len(nums) - 1):

			for j in range(i, len(nums)):


				temp_profit = nums[j] - nums[i]

				max_profit = max(max_profit,temp_profit)

		return max_profit


	def maxProfit_optim(self,nums):
		"""
		The function to find the max profit in optimum approach

		[7,1,5,3,6,4]
		"""

		#base case 


		if not prices:
			return 0
		
		min_price = prices[0]
		max_profit = 0
		
		for price in prices:
			min_price = min(min_price, price)
			max_profit = max(max_profit, price - min_price)
		
		return max_profit








if __name__ == '__main__':
	
	sol = Solution()


	print(sol.maxProfit_optim(prices))
