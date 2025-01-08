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


class Solution_slow():
	"""
	works , but slow solution
	"""

	def __init__(self):

		self.memo = {}
		self.res_lst = []

	def helper_dfs(self,val, count):
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

			self.helper_dfs(val + coin , count + 1 )



	def coinChange(self, coins, amount) :
		"""
		The function to find the coin chnage 
		"""

		self.coins = coins
		self.amount = amount

		
		if self.amount == 0 :

			return 0 

		#constraints 
		if len(self.coins) == 1 :

			if self.coins[0] == self.amount :

				return 1



		#make the vars 
		val = 0 
		count = 0

		#make the recurion call 
		self.helper_dfs(val,count)

		#print(self.res_lst)

		#return -1 if no value exists
		if not self.res_lst:

			return -1 


		self.res_lst.sort()

		return self.res_lst[0]




class Solution_slow2():
	"""
	works , but slow solution
	"""

	def __init__(self):

		self.memo = {}
		self.res_lst = []

	def helper_dfs(self,val, coin_tuple, count):
		"""
		The function to do the dfs for the tree
		"""

		#base case
		if val > self.amount :

			return

		if coin_tuple in self.memo :

			self.helper_dfs(self.memo[coin_tuple] + val, coin_tuple + (coin,) , count + 1 )


		if val == self.amount:

			self.res_lst.append(count)

			return


		#add the value in memo
		self.memo[coin_tuple] = val


		#do the recursive call 
		for coin in self.coins:

			if val + coin <= self.amount :

				self.helper_dfs(val + coin , coin_tuple + (coin,), count + 1 )



	def coinChange(self, coins, amount) :
		"""
		The function to find the coin chnage 
		"""

		self.coins = coins
		self.amount = amount

		
		if self.amount == 0 :

			return 0 

		#constraints 
		if len(self.coins) == 1 :

			if self.coins[0] == self.amount :

				return 1



		#make the vars 
		val = 0 
		count = 0
		coin_tuple = ()

		#make the recurion call 
		self.helper_dfs(val, coin_tuple, count)

		#print(self.res_lst)

		#return -1 if no value exists
		if not self.res_lst:

			return -1 

		print(self.memo)


		self.res_lst.sort()

		return self.res_lst[0]




class Solution_slow3():
	"""
	Accepted in leetcode but slow soln
	"""

	def __init__(self):

		self.memo = {}
		self.min_count = float("inf")


	def helper_dfs(self,val,count):
		"""
		The function to do the dfs for coin change

		"""
		
		#base case 
		if val > self.amount :

			return

		if val == self.amount :

			self.min_count = min(self.min_count , count)

			return

		# If the current count is already worse than the best solution, prune
		if count >= self.min_count:
			return

		if val in self.memo and self.memo[val] <= count :

			return

		#add in memo
		self.memo[val] = count

		#make the recursive call
		for coin in self.coins :

			if (val + coin) <= self.amount :

				self.helper_dfs(val + coin , count + 1 )




	def coinChange(self,coins,amount):
		"""
		The function to coun the coins needed
		"""

		self.coins = sorted(coins, reverse=True)  # Sort coins in descending order
		self.amount = amount

		#constarints
		if (len(self.coins) == 1) :

			if self.coins[0] == self.amount :

				return 1

		if self.amount == 0 :

			return 0

		#make vars 
		val = 0 
		count = 0 

		self.helper_dfs(val,count)

		if self.min_count == float("inf") :

			return -1 

		return self.min_count





sol = Solution()
print(sol.coinChange([1,2,5],11))



