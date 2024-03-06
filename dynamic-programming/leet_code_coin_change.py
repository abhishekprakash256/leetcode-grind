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



"""



class Solution():

	def coinChange_brute_force(self,coins,amount):
		"""
		The function to calculate the least number of the coin that can be given out 
		"""
		pass
