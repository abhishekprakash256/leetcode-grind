"""
The file is to traverse the graph using the DFS and BFS , all kinds of graph
"""


## make the tree 
class Node():

	def __init__(self, val):

		self.val = val
		self.left = None
		self.right = None



#connecting the tree
first = Node(1)
second = Node(2)
third = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)



#connect the node -- 
first.left = second 
first.right = third 
second.left = four
second.right = five
third.left = seven
third.right = eight




class TreeHelper():

	def dfs_traversal(self, node):
		"""
		The function to traverse the tree using dfs
		"""

		#the return case
		if not node :

			return

		#traverse the node
		if node :

			print(node.val)

			#traverse nodes

			self.dfs_traversal(node.left)

			self.dfs_traversal(node.right)


	def bfs_traversal(self , node ):
		"""
		The function to traverse the tree using bfs traversal
		"""

		#make the queue 
		queue = [node]

		#traverse the queue
		while queue :

			curr_node = queue.pop(0)

			if curr_node :

				print(curr_node.val)

				queue.append(curr_node.right)

				queue.append(curr_node.left)




#call the main function 

if __name__ == "__main__" :

	tree_helper = TreeHelper()

	dfs_res = tree_helper.dfs_traversal(first)

	print(dfs_res)

	bfs_res = tree_helper.bfs_traversal(first) 

	print(bfs_res)








































