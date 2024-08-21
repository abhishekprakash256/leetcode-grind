"""
102. Binary Tree Level Order Traversal


Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []


"""


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

	def bfs(self,node):
		"""
		The bfs traversal of the tree
		"""

		#base case 
		if not node:
			return []

		
		#vars 
		queue = [node]
		node_lst = []

		#start traversal 
		while queue:

			curr_node = queue.pop(0)

			node_lst.append(curr_node.val)

			if curr_node.left:

				queue.append(curr_node.left)

			if curr_node.right:
				queue.append(curr_node.right)


		return node_lst

	def bfs_list(self,node):
		"""
		The bfs travesal and append in the list as per level
		"""

		#base case 
		if not node:
			return []

		#vars
		queue = [node]
		node_lst = []

		#start traversal
		while queue:

			level = []
			level_length = len(queue)

			for i in range(level_length):

				curr_node = queue.pop(0)
				level.append(curr_node.val)

				if curr_node.left:
					
					queue.append(curr_node.left)

				if curr_node.right:
					queue.append(curr_node.right)

			node_lst.append(level)

		return node_lst









if __name__ == "__main__":

	sol = Solution()
	print(sol.bfs(root))
	print(sol.bfs_list(root))










