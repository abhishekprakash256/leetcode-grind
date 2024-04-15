"""
make the subset of the given array 
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


"""
[1,2,3]


lst = []
res = []

backtrack



"""


class Solution:
	def subsets(self,nums):
		def backtrack(start, path):
			result.append(path[:])
			for i in range(start, len(nums)):
				path.append(nums[i])
				backtrack(i + 1, path)
				path.pop()
		
		result = []
		backtrack(0, [])
		return result