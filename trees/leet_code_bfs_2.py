"""

The iterative implemenation of the bfs traveral of the tree
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

	def bfs_traversal(self,node):
		"""
		The bfs traversal of the tree
		"""

		#base case 
		if not node:
			return []


		#vars 
		node_lst = []
		queue = [node]

		while queue:

			curr_node = queue.pop(0)

			node_lst.append(curr_node.val)

			if curr_node.left:

				queue.append(curr_node.left)

			if curr_node.right:

				queue.append(curr_node.right)


		return node_lst



if __name__ == "__main__":

	sol = Solution()

	print(sol.bfs_traversal(root))


