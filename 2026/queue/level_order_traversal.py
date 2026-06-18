"""
using the level order traversal

"""


#make the traversal 

from collections import deque


class Node():

	def __init__(self,val):

		self.val = val
		self.left = None
		self.right = None



#make the nodes 
root = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)


#connect the node 
root.left = second
root.right = third
second.left = fourth
second.right = fifth
third.left = sixth
third.right = seventh



class TreeHelper():

	def level_order_traversal(self, root : Node) :
		"""
		The level order traversal for the tree
		"""

		#edge case not have a node
		if not root:
			return [[]]

		#make the queue
		queue = deque([root])

		#result list
		res = []

		#start traversal
		while queue :

			#get the queue length 
			length = len(queue)

			#the level list
			level = []

			#traverse the width 
			for _ in range(length) :

				node = queue.popleft()

				level.append(node.val)

				if node.left:

					queue.append(node.left)

				if node.right:

					queue.append(node.right)

			res.append(level)

		return res




treehelper = TreeHelper()

res = treehelper.level_order_traversal(root)

print(res)


