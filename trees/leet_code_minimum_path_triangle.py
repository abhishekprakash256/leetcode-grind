"""
Return the minimum path from the bottom to down
"""

class Solution():

	def minimumTotal(self,triangle):
		"""
		The function to find the minimum triangle
		"""

		dp = [0] * (len(triangle) + 1)

		for row in triangle[::-1]:

			for i,n in enumerate(row):

				dp[i] = n + min(dp[i], dp[i+1])


		return dp[0]




