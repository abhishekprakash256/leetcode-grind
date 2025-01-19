"""
make the tree and exp with the dfs and bfs 
"""
from collections import deque


class TreeNode():
	def __init__(self,val,left = None,right = None):

		self.val = val
		self.left = left
		self.right = right


# Example tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))



class Tree_Helper():

	def tree_dfs_rec(self,node):
		"""
		The function to print the tree in dfs
		"""

		#base case
		if not node:

			return

		#print the value of the node
		print(node.val)

		self.tree_dfs_rec(node.left)

		self.tree_dfs_rec(node.right)

		return "Tree print is done by dfs rec"


	def tree_dfs_iter(self,node):
		"""
		The function to make the tree dfs iteration
		"""
		
		#base case 
		if not node:

			return

		#make the stack and add value
		stack = deque([node])

		while stack :

			temp_node = stack.pop()

			if temp_node :

				print(temp_node.val)

			if temp_node.right :

				stack.append(temp_node.right)

			if temp_node.left :

				stack.append(temp_node.left)


		return "The tree is printed by dfs iter"




	def tree_bfs(self,node):
		"""
		The function to print the tree using bfs
		"""

		#base case 
		if not node:

			return

		#make the queue and add the first node
		queue = deque([node])

		while queue:

			temp_node = queue.popleft()

			#print the val
			if temp_node:
				print(temp_node.val)

			#append the node
			if temp_node.left:
			
				queue.append(temp_node.left)

			if temp_node.right:

				queue.append(temp_node.right)


		return "Tree print is done as bfs"


	def tree_bfs_lst(self,node):
		"""
		The fuction to append the node in list at per level
		"""

		#base case 
		if not node:

			return []


		#make the result list 
		result = []

		#make the queue
		queue = deque([node])

		#start the loop over queue
		while queue:

			temp_lst = []

			for _ in range(len(queue)):

				temp_node = queue.popleft()

				if temp_node:

					temp_lst.append(temp_node.val)

				if temp_node.left :

					queue.append(temp_node.left)

				if temp_node.right :

					queue.append(temp_node.right)


			result.append(temp_lst)


		return result









helper = Tree_Helper()

print(helper.tree_dfs_rec(root))

print(helper.tree_dfs_iter(root))

print(helper.tree_bfs(root))

print(helper.tree_bfs_lst(root))