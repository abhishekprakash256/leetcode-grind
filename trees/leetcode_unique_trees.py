"""
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

"""


"""
Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]]


"""


"""
approach -- 

using a recursive apprioach 

result = []

if len(temp_lst) == n :

	result.append(temp_lst)

append the left and right subtree

make node and add the node and calcukate the level 

as the level reaches then cut 

"""




class Solution_combinations():

	def __init__(self):

		self.result = []

	def helper_dfs(self,temp_lst):
		"""
		The function to make combinations
		"""

		#base case 
		if len(temp_lst) == self.n :

			self.result.append(temp_lst)

			return

		#make the recureive call
		for i in range(1,self.n + 1) :

			if i not in temp_lst:
			
				self.helper_dfs(temp_lst + [i])


		


	def make_combinations(self,n):
		"""
		The function to make the possible combinations
		"""

		self.n = n

		#constraints case 
		if self.n == 0 :

			return []

		if self.n == 1 :

			return [[1]]


		temp_lst = []

		#make the recursive call
		self.helper_dfs(temp_lst)

		return self.result




sol = Solution_combinations()

print(sol.make_combinations(3))

#[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

#output -> [1,3,2] , [1,2,3] , [2,1,3] , [3,2,1] ,[3,1,2]

# [2,3,1]

class TreeNode:
	"""
	The tree node class to make the tree
	"""

	def __init__(self, val=0, left=None, right=None):

		self.val = val

		self.left = left

		self.right = right



class Solution():

	def __init__(self):

		self.result = []


	def helper_dfs(self,node):
		"""
		The helper function of the dfs
		"""
		
		#base case 
		if left >= right :

			result.append(temp_lst)

			return

		#make the node 
		left = TreeNode()
		right = TreeNode()

		








	def generateTrees(self, n: int) :
		"""
		The function to make the tree

		"""
		
		self.n = n

		#constaints case 

		if self.n == 1 :

			return [[1]]

		#make the left and right tree
		left = 1
		right = self.n

		#make the temp lst
		temp_lst = []

		#make the recursive request
		self.helper_dfs(left,right,temp_lst)

		#return the result
		return self.result



 

















