"""

Given the root of a binary tree, return the inorder traversal of its nodes' values.

in dfs
left -> root -> right 
"""

"""
approach 

dfs using the inorder 
recursion 

make a list and pass the node to the helper function 

two function or method 

def helper(self,node_lst,node)
def inorderTraversal(self,root)


base case 
if not node:
	return node



"""


class Solution():

	def helper_dfs(self,node,node_lst):
		"""
		The helper function to make the dfs traversaL
		"""

		if node:

			self.helper_dfs(node.left,node_lst)

			node_lst.append(node.val)

			self.helper_dfs(node.right,node_lst)

	def inorderTraversal(self,root):
		"""
		The main traversal function
		the code passed leetcode
		"""

		#base case
		if not root:
			return None

		node_lst = []

		self.helper_dfs(root,node_lst)

		return node_lst