"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""


class Node:

	def __init__(self,val = None, left = None, right = None , next = None):

		self.val = val
		self.left = left
		self.right = right

#make node 

root = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(7)


#connect the trees

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5



class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		"""
		Perform level-order traversal of a binary tree and return a list of lists.
		"""
		# Base case: If the tree is empty, return an empty list
		if not root:
			return []

		# Initialize the queue with the root node
		queue = [root]
		res_lst = []

		# Loop until the queue is empty
		while queue:
			temp_lst = []  # To store the current level's node values
			level_size = len(queue)  # Number of nodes at the current level

			for _ in range(level_size):
				node = queue.pop(0)  # Dequeue the next node

				# Append the current node's value to the level list
				if node:
					temp_lst.append(node.val)

					# Add the node's children to the queue for the next level
					queue.append(node.left)
					queue.append(node.right)

			# Append the completed level to the result only if it's non-empty
			if temp_lst:
				res_lst.append(temp_lst)

		return res_lst




