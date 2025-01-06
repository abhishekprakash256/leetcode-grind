"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

"""
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45

"""


"""
approach -- 

base case 

0 step = 1 

1 step = 

2 step = 2 ways 


using DP and recursion 


"""

class Solution():

	def climbStairs(self,n) :
		"""
		The function to find the number of steps req to climb stairs 
		The dynamic solution
		passes leetcode 
		"""

		#base case 

		if n == 1 :
			return 1 

		if n == 2 :
			return 2 

		#make the dp araay
		steps = [0] * n

		#make the steps count
		steps[0] , steps[1] = 1 , 2

		for i in range(2,n) :

			steps[i] = steps[i-1] + steps[i-2]

		return steps[-1]



class Solution_rec():
	"""
	passes leetcode
	"""

	def __init__(self):

		self.memo = {}

	def climbStairs(self,n):
		"""
		The function to climb the stairs using recursion
		"""

		#base case 

		if n == 1 :
			return 1 

		if n == 2 :
			return 2 

		if n in self.memo:
			return self.memo[n]

		steps = self.climbStairs(n-2) + self.climbStairs(n-1)

		#add the steps value in memo
		self.memo[n] = steps

		return steps



sol = Solution()

print(sol.climbStairs(3))








