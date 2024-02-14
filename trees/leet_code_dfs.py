"""
the dfs traversal of the tree using the iterative and recursive approach 
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

	def dfs_iterative(self,node):
		"""
		The dfs iterative appraoch of the tree
		"""

		#make the initial list 
		res_lst = []

		if not node:
			return res_lst


		#make the queue
		queue = []
		queue.append(node)

		while queue:

			node = queue.pop()

			if node:
				res_lst.append(node.val)

			if node.right:
				queue.append(node.right)

			if node.left:
				queue.append(node.left)

		return res_lst



if __name__ == '__main__':
	sol = Solution()

	res_iterative = sol.dfs_iterative(root)

	print(res_iterative)

