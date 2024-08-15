"""
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

root = [3,9,20,null,null,15,7]
Output: 3
"""



"""
approach 

1. using recursion 

	- height = 0 
	  base caes 
		- if not node.left and not node.right:
			return 0 

		elif node.left:
			height(height + 1 , node.left)

		elif node.right:
			height( height + 1, node.right)

		else:
			hegight( height +1 , node.right)
			height( height +1 , node.left)

	  return height




let's code



class Solution:
	def calc_height(height,node):

		#base case 
		if not node.left and node.right:
			return 0

		elif node.left:
			self.calc_height(height + 1 , node.left)

		elif node.left:
			self.calc_height(height + 1 , node.left)

		else:
			hegight( height +1 , node.right)
			height( height +1 , node.left)

		return height			




	def maxDepth(self, root: Optional[TreeNode]) -> int:

		#base case 
		if not node:
			return 0 

		return self.calc_height(self,0,node)

	
"""




class Solution:
	def calc_height_wrong(height,node):

		#base case 
		if not node.left and node.right:
			return 0

		elif node.left:
			self.calc_height(height + 1 , node.left)

		elif node.left:
			self.calc_height(height + 1 , node.left)

		else:
			hegight( height +1 , node.right)
			height( height +1 , node.left)

		return height			




	def maxDepth_wrong(self, root: Optional[TreeNode]) -> int:

		#base case 
		if not node:
			return 0 

		return self.calc_height(self,0,node)


	def calc_height(self, node):
		"""
		passed the leet code
		"""
		# Base case: If the node is None, return height as 0
		if not node:
			return 0

		# Recursively calculate height of left and right subtrees
		left_height = self.calc_height(node.left)
		right_height = self.calc_height(node.right)

		# Return the maximum of left and right heights plus 1 for the current node
		return max(left_height, right_height) + 1

	def maxDepth(self, root: Optional[TreeNode]) -> int:
		# Base case: If the tree is empty, return 0
		if not root:
			return 0

		# Calculate the maximum depth using calc_height function
		return self.calc_height(root)



		