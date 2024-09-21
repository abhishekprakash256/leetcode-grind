"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

"""

"""
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Input: nums = [0,1]
Output: [[0,1],[1,0]]

"""


"""
approach -- 



"""


class Solution():

	def __init__(self):
		self.res_lst = []


	def helper(self,start_lst):
		"""
		The helper funciton
		"""

		#base case 
		if len(start_lst) == len(self.nums):
			self.res_lst.append(start_lst[:])
			return None


		for i in self.nums:

			if i not in start_lst:

				start_lst.append(i)

				self.helper(start_lst)

				start_lst.pop()


	def permute(self,nums):
		"""
		The permute function
		works in leet code and passes 
		"""

		self.nums = nums


		#base case
		if len(nums) == 1:
			return [nums]

		start_lst = []

		self.helper(start_lst)


		return self.res_lst




