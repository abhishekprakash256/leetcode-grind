"""
Given the root of a binary tree, invert the tree, and return its root.

"""

"""
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]


Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

"""



"""
approach - using recursion 

#base case

if not node 
	return None 



if node 
	node.left , node.right = node.right , node.left 






"""

class Solution(object):
	def invertTree(self, root):
		"""
		:type root: Optional[TreeNode]
		:rtype: Optional[TreeNode]
		"""
		
		#base case 
		if not root : 

			return None 



		#if node exists 
		if root : 

			root.left , root.right = root.right , root.left

			self.invertTree(root.left)
			
			self.invertTree(root.right)


		return root 

		