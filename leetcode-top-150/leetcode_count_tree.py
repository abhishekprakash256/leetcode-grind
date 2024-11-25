"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
"""


"""

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1


"""


"""
approach - 

using dfs 

count = 0 
as global


"""


class Solution_slow(object):

	def helper_dfs(self,node):

		if not node:
			return 0 

		if node :

			self.count+=1

			self.helper_dfs(node.left)
			self.helper_dfs(node.right)




	def countNodes(self, root):
		"""
		:type root: Optional[TreeNode]
		:rtype: int
		"""

		#base case 
		if not root:
			return 0 


		if not root.left and not root.right :
			return 1 


		self.count = 0

		self.helper_dfs(root)

		return self.count





class Solution(object):
	def countNodes(self, root):
		"""
		Count the number of nodes in a binary tree using DFS.
		:type root: Optional[TreeNode]
		:rtype: int
		"""
		if not root:
			return 0  # Base case: no nodes in an empty tree

		# Count the current node, left subtree, and right subtree
		return 1 + self.countNodes(root.left) + self.countNodes(root.right)
