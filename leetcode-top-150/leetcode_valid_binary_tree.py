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

class Solution(object):

	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""

		#base case 
		if root.left is None and root.right is None :

			return True

		#make the queue 
		queue = [root]

		while queue : 

			curr_node = queue.pop(0)

			if curr_node.left :

				queue.append(curr_node.left)

				if curr_node.val > curr_node.left.val :

					return False


			if curr_node.right:

				queue.append(curr_node.right)

				if curr_node.val < curr_node.right.val :

					return False

		return True











