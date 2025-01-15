"""
Given an integer array nums that may contain duplicates, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

"""
Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""

"""
approach  --- 

using recursion 

result is a set 

check every time we add a list 

add a empty list as well 

increase the i 

"""

class Solution():

	def __init__(self):

		self.result = []
		#self.mapper = {}

	def helper_dfs(self,i, temp_lst) :
		"""
		The helper dfs for making the subsets 
		"""

		#base case 
		if len(temp_lst) == len(self.nums) :

			self.result.append(temp_lst)

			return

		if temp_lst in self.result:

			return

		#make the recursion call
		for j in range(i,len(self.nums)):

			if temp_lst not in self.result :

				self.result.append(temp_lst.append(self.nums[j]))

				self.helper_dfs(i+1,temp_lst + [self.nums[j]])

			 

	def subsetsWithDup(self,nums) :
		"""
		The function to find the subsets 

		"""
		self.nums = nums

		#constarints 
		if len(nums) == 1 :

			return [[],[nums[0]]]


		#make the vars 
		i = 0
		temp_lst = []

		self.helper_dfs(i,temp_lst)

		return list(self.result)





test = {}

test[[1]] = True

