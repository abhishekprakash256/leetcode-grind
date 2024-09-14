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




class Solution2():

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



class Solution3:

    def __init__(self):
        self.memo = {}  # Memoization dictionary to store results for subproblems.

    def helper(self, rem, coins):
        """
        The helper function to find the minimum number of coins using memoization.
        """
        # Base case: if remaining amount is less than 0, return an impossible large value.
        if rem < 0:
            return float('inf')  # Return infinity to signify that it's not possible.

        # Base case: if remaining amount is 0, no more coins are needed.
        if rem == 0:
            return 0

        # If we have already computed the result for this amount, return it.
        if rem in self.memo:
            return self.memo[rem]

        # Try each coin and take the minimum number of coins needed.
        min_coins = float('inf')
        for coin in coins:
            result = self.helper(rem - coin, coins)
            min_coins = min(min_coins, result + 1)  # Add 1 to include the current coin.
            self.memo[rem] = min_coins

        # Memoize the result for the current remaining amount.
        
        return min_coins

    def coinChange(self, coins, amount):
        """
        passed leetcode
        The main function to find the minimum number of coins to make up the amount.
        """
        if amount == 0:
            return 0

        # Compute the result using the helper function.
        result = self.helper(amount, coins)

        # If the result is infinity, it means it's impossible to make the amount.
        return result if result != float('inf') else -1



class Solution:
    def coinChange(self, coins, amount):
    	#fastest solution accepted in leetcode
        # Create a DP array to store the minimum coins for each amount.
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make amount 0.
        
        # Loop over each coin and compute the minimum coins for each amount.
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still infinity, return -1 (not possible to make amount).
        return dp[amount] if dp[amount] != float('inf') else -1


		
























