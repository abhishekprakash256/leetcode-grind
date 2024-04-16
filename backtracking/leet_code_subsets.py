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


class Solution2:
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
	




class Solution():
	def __init__(self):
		self.res = []
		self.lst = []

	
	def backtrack(self,path):
		"""
		The function to backtrack 
		"""
		if (path) >= len(self.nums):
			self.res.append(self.lst.copy())
			return 
		
		self.lst.append(self.nums[path])
		self.backtrack(path+1)

		self.lst.pop()
		self.backtrack(path+1)
	
	def subsets(self,nums):
		"""
		The main function 
		"""

		self.nums = nums

		self.backtrack(0)

		return self.res

        





