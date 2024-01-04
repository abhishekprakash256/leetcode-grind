"""
the problem of findindg the number of steps needed to climb the stair case 
one and two steps can be taken at a time 
the steps with same number but different order are consider differnt
"""

#the problem can be vislauized using a tree soln which the root will be the number of the stps we are in 
#the edge will be the steps that we took to reach there 
#using the recursion and depth first search 
#we can use the DP for the storage of the steps so the steps are not repeacted 

class Solution():
	def climbStairs(self,n):
		"""
		find the minimum number of stairs 
		"""
		#initilaize the variables 
		one, two = 1,1

		for i in range(n-1):

			temp = one 
			one = one + two
			two = temp 

		return one
