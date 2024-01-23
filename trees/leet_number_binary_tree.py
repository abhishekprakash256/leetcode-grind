"""
FInd the number of the binary tree that can be formed from the number of given node
"""


#incorreect solution 


class Solution():


	#incorect soln
	def numTrees_incorrect(self,nums):
		"""
		The function to find the number of trees that can be formed 
		"""

		#base cases

		if nums == 0 : 
			return 0 

		if nums == 1: 
			return 1 

		if nums == 2:
			return 2 


		#make the recuesive calls 
		return nums*(self.numTrees(nums-2)) + self.numTrees(nums-1)

	def numTrees(self,n):
		if n <= 0:
			return 0

		# Initialize an array to store the number of unique BSTs for each number of nodes
		dp = [0] * (n + 1)
		dp[0], dp[1] = 1, 1

		# Calculate the number of unique BSTs for each number of nodes from 2 to n
		for i in range(2, n + 1):
			for j in range(1, i + 1):
				# The number of BSTs is the product of the number of left and right subtrees
				dp[i] += dp[j - 1] * dp[i - j]

		return dp[n]


if __name__ == "__main__":
	sol = Solution()

	res = sol.numTrees(4)

	print(res)