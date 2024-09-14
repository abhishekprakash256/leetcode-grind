"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


"""

coins = [1,2,5]
amount = 11
out = 3 

coins2 = [2]
amount2 = 3
out2 = -1

coins3 = [1]
amount3 = 0
out3 = 0 



"""
Algo -- 

recursion 

costraint
if amount == 0:
	return 0 

loop over the vales 

#base case 

if temp_sum == amount: 
	return True

if temp_sum > amount:
	return False 



temp_sum = 0 


for change in coins:
	res = self.helper(change,temp_sum, amount)

return res


#helper function 

#base case 
if temp_sum == amount:
	return True 

if temp_sum > amount :
	return False


for coin in chnage:
	res = self.helper(coin,temp_sum + coin,amount)

return res



"""



class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize memoization dictionary
        #passes the leetcode
        memo = {}

        # Call the recursive function with memoization
        return self.helper(coins, amount, memo)

    # Helper function to handle recursion and memoization
    def helper(self, coins: list[int], rem: int, memo: dict) -> int:
        # If remaining amount is negative, return -1 (invalid)
        if rem < 0:
            return -1
        # If remaining amount is 0, no coins are needed
        if rem == 0:
            return 0
        # If result is already computed for rem, return it from memo
        if rem in memo:
            return memo[rem]

        # Initialize the minimum cost to infinity
        min_cost = float('inf')

        # Try every coin and check the result of the subproblem (rem - coin)
        for coin in coins:
            res = self.helper(coins, rem - coin, memo)
            if res != -1:
                min_cost = min(min_cost, res + 1)

        # Store the computed result in memo (either the minimum cost or -1 if no solution)
        memo[rem] = min_cost if min_cost != float('inf') else -1
        return memo[rem]

		
class Solution2:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        passes the leetcode and fasster
        """
        # Initialize a dp array with amount + 1 as default value (amount + 1 is greater than any possible answer)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make amount 0

        # Iterate through each amount from 1 to the target amount
        for i in range(1, amount + 1):
            # Check each coin denomination
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)  # Find the minimum number of coins

        # If dp[amount] is still set to the initial value, return -1 (means it's impossible)
        return dp[amount] if dp[amount] != amount + 1 else -1





