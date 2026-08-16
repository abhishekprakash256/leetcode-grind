"""
Given an integer array nums of unique elements, return all possible (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

"""
Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.


"""


"""
approach -- 

make the tree -- 

start with empty list 

option to choose all 

how we do the length ? 

we can do i + 1 start , so that get the next position 

"""

from typing import List



class Solution:

	def __init__(self):
		
		self.res = []

	def _helper(self, start , res_lst) : 
		"""
		The helper function for the recursion depth
		"""

		#make the base case 
		if start > len(self.nums) - 1 :

			self.res.append(res_lst)

			return


		#append the curr list
		self.res.append(res_lst)


		#make the recursion call
		for i in range( start , len(self.nums) ) :


			self._helper(i + 1 , res_lst + [self.nums[i]] )


	def subsets(self, nums: List[int]) -> List[List[int]]:
		"""
		The function to find the subsets
		"""

		self.nums = sorted(nums)

		#make the recustion call
		self._helper(start = 0  , res_lst = [] )

		#return the results
		return self.res







#testing the solution 
if __name__ == '__main__':

	sol = Solution()

	res = sol.subsets( nums = [1,2,3] )

	print(res)


	














