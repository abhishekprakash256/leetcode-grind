"""
the dfs traversal of the tree using the iterative and recursive approach

"""

# Example binary tree
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7

#1,2,4,5,3,6,7


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

		
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)





class Solution():

	def helper_dfs(self,node,node_lst):
		"""
		The fucntion to return the dfs traversal of the tree
		"""

		if node:

			node_lst.append(node.val)
			
			self.helper_dfs(node.left,node_lst)

			self.helper_dfs(node.right,node_lst)
		



	def dfs_rec(self,node):
		"""
		The function to give the recursive dfs traversal for tree
		The code  works and tested
		"""
		#base case 
		if not node:
			return []

		if node.left is None and node.right is None:
			return [node.val]

		node_lst = []

		self.helper_dfs(node,node_lst)

		return node_lst



	def dfs_iter(self,node):
		"""
		The fucntiotn to print the dfs for the iterative
		The fuction is working
		"""

		#base case 
		if not node:
			return []


		#the initial vars
		node_lst = []
		stack = [node]

		while stack:

			curr_node = stack.pop()

			node_lst.append(curr_node.val)

			if curr_node.right:

				stack.append(curr_node.right)

			if curr_node.left:

				stack.append(curr_node.left)

		return node_lst



















if __name__ == "__main__":
	sol = Solution()

	print(sol.dfs_rec(root))
	print(sol.dfs_iter(root))
