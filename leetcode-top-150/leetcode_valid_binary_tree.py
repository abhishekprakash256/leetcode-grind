"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

	The left
	subtree
	of a node contains only nodes with keys less than the node's key.
	The right subtree of a node contains only nodes with keys greater than the node's key.
	Both the left and right subtrees must also be binary search trees.

"""


"""
Input: root = [2,1,3]
Output: true


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""

class Solution:

	def isValidBST(self, node: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
		"""
		Passes leetcode
		"""
		# Base case: An empty tree is a valid BST
		if not node:
			return True

		# The current node's value must be in the range (low < node.val < high)
		if not (low < node.val < high):
			return False

		# Recursively check the left and right subtrees with updated ranges
		return (self.isValidBST(node.left, low, node.val) and self.isValidBST(node.right, node.val, high))











