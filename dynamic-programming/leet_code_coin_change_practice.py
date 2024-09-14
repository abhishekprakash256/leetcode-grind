"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""


"""

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

"""

"""

Input: coins = [2], amount = 3
Output: -1
"""




class Solution():

	def helper_brute_force(self, rem, coins, count, lst):
		"""
		The helper function to do the DFS.
		"""

		# Base case: if remaining amount is negative, return.
		if rem < 0:
			return

		# Base case: if remaining amount is 0, add the current count to the result list.
		if rem == 0:
			lst.append(count)
			return

		# Recursive case: try each coin and recurse.
		for coin in coins:
			self.helper(rem - coin, coins, count + 1, lst)


	def coinChange_brute_force(self, coins, amount):
		"""
		The main function to find the minimum number of coins to make up the amount.
		The soln is coorrect but time limit exceeded 
		"""
		# If amount is zero, no coins are needed.
		if amount == 0:
			return 0

		# If there's only one coin, check if it divides the amount exactly.
		if len(coins) == 1:
			if amount % coins[0] == 0:
				return amount // coins[0]
			else:
				return -1  # No valid way to make the amount with one coin.

		# Initialize the result list.
		res_lst = []
		count = 0

		# Start recursion from each coin.
		for coin in coins:
			self.helper(amount - coin, coins, count + 1, res_lst)

		# If no valid combinations were found, return -1.
		if not res_lst:
			return -1

		# Return the minimum count of coins needed.
		return min(res_lst)



	def helper()




















