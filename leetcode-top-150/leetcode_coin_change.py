"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


"""

"""

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


"""

"""
approach -- 

using the recursion -- 

do a dst and memo for faster traversal

5 + 5 + 1 = 11 


carry the count return the lowest count 

res_lst gets all the count sort it and return the first value


res_lst = []

count = 0 

val = 0 


base case

"""


class Solution():

	def __init__(self):

		self.memo = {}
		self.res_lst = []

	def helper_dfs(self,count, val):
		"""
		The function to do the dfs for the tree
		"""

		#base case
		if val > self.amount :

			return 

		if val == self.amount:

			self.res_lst.append(count)

			return

		#add in the memo 


		#do the recursive call 
		for coin in self.coins:

			val += coin
			count += 1 

			self.helper_dfs(val,count)






	def coinChange(self, coins, amount) :
		"""
		The function to find the coin chnage 
		"""

		self.coins = coins
		self.amount = amount

		#constraints 
		if len(self.coins) == 1 :

			if self.coins[0] == self.amount :

				return 1

			elif self.coins[0] > self.amount :

				return -1 

			else :

				val = 0
				count = 0 

				while val < amount :

					val += self.coins[0]
					count += 1 

					if val == amount :

						return count



		#make the vars 
		val = 0 
		count = 0

		#make the recurion call 
		self.coinChange(val,count)

		return self.res_lst[0]









