"""
leet code invert the binary tree
"""

class Solution():

	def invertTree(self,node):
		"""
		invert a binary tree
		"""

		if not node:
			return None

		node.left.val , node.right.val = node.right.val, node.left.val

		self.invertTree(node.left)
		self.invertTree(node.right)

		return node



