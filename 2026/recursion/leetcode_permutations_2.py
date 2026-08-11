"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""

"""
Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
[1,2,1],
[2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""

"""
approach -- 



"""

class Solution():

	def __init__(self):

		self.res = []


	def _helper(self, idx , res_lst):
		"""
		The function for dfs tree
		"""

		#base case 
		if len(res_lst) == len(self.nums) :

			self.res.append(res_lst)

			return


		#make the stack
		for i in range( len(self.nums) ):

			if i == idx :

				continue

			self._helper( i , res_lst + [self.nums[i]])


	def permuteUnique(self, nums):
		"""
		The function to find the unique permutations
		"""

		self.nums = nums

		#call the helper function
		self._helper(0 , [] )

		#return the result
		return self.res


#testing 

#testing the solution 
if __name__ == '__main__':

	sol = Solution()

	res = sol.permuteUnique( nums = [1,1,2] )

	print(res)


