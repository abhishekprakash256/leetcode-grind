"""
make the bfs traversal of the tree

"""

# Example binary tree
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7



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

	def bfs_iterative(self,node):
		"""
		The function to bfs iterative of the tree
		"""

		#base case 
		if not node:
			return None

		#initilaize the vars

		queue = []
		queue.append(node)
		res_lst = []

		while queue:

			node = queue.pop(0)

			if node:

				res_lst.append(node.val)

			if node.left:

				queue.append(node.left)

			if node.right:

				queue.append(node.right)


		return res_lst

		
		

if __name__ == '__main__':
	sol = Solution()

	res_iterative = sol.bfs_iterative(root)

	print(res_iterative)

	print(res_recursive)