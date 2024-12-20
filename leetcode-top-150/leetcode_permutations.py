"""

Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order
"""


"""
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""


class Solution:
	"""
	Passes leet code
	"""

	def __init__(self):

		self.permutations_lst = []

	def helper_dfs(self,temp_lst):
		"""
		The helper function to do the dfs 
		"""
		#base case 
		if len(temp_lst) == len(self.nums) :

			#append in the main list
			self.permutations_lst.append(temp_lst)
			return


		#make the recursive call
		for j in self.nums :

			#start the call
			if j not in temp_lst:

				self.helper_dfs(temp_lst + [j])



	def permute(self, nums: List[int]) -> List[List[int]]:
		"""
		The main permute function
		"""

		self.nums = nums
		
		#base case 
		if len(nums) == 1:
			return [[nums[0]]]

		#start the recursion
		self.helper_dfs([])

		#return the combined list 
		return self.permutations_lst

