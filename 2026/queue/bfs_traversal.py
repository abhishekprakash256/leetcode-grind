"""
The traversal of the bfs tree

"""

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




#make the traversal 

from collections import deque


class TreeHelper():

	def bfs(self,root : Node) :
		"""
		The function for the bfs traversal
		"""

		#make the queue
		queue = deque()
		
		#append the root		
		queue.append(root)

		#make the list
		nodes = []

		while queue:

			node = queue.popleft()

			nodes.append(node.val)

			if node.left :

				queue.append(node.left)

			if node.right :

				queue.append(node.right)

		return nodes



treehelper = TreeHelper()


res = treehelper.bfs(root)

print(res)