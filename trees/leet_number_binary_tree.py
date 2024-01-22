"""
FInd the number of the binary tree that can be formed from the number of given node
"""


#incorreect solution 


class Solution():

	def numTrees(self,nums):
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



if __name__ == "__main__":
	sol = Solution()

	res = sol.numTrees(4)

	print(res)