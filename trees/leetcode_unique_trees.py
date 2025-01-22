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

we can use a set of numbers like backtracking 

and pick the value and add it 




"""


class TreeNode:
	"""
	The tree node class to make the tree
	"""

	def __init__(self, val=0, left=None, right=None):

		self.val = val

		self.left = left

		self.right = right







