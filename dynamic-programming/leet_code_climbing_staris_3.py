"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


"""
approach - 

breke the problem into small subprobkems and I can buiuold on top of that 

if n == 1 :
	ways = 1 

if n == 2 :
	ways = 2 

if n == 3:
	ways = n of 1 + n of 2 


1. Apprach - 

recursion - 

base case 
if n == 0 :
	return 0 

if n == 1 :
	return 1 

if n == 2 : 
	return 2 

self.ways(n-1) + self.ways(n-2)


"""



class Solution(object):

	def climbStairs_recursion(self, n):
		"""
		using recursion
		:type n: int
		:rtype: int
		"""

		#base case 
		if n == 0:
			return 0 

		if n == 1:
			return 1

		if n == 2:
			return 2

		return self.climbStairs(n-1) + self.climbStairs(n-2)


    def climbStairs(self, n):
        """
        using dp
        """
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
