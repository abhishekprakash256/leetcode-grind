"""
The file is to traverse the graph using the DFS and BFS , all kinds of graph
"""


from collections import deque


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





"""
using the adjaceny list graph 
"""


class AdjacenyListGraph():

	def __init__(self):

		self.graph = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

		self.visited = set()


	def dfs_traversal(self):
		"""
		The function to traverse the graph using the adjaceny list
		"""
		node = 0 

		self.dfs_helper(node)

	

	#make the helper traversal
	def dfs_helper(self, node) :
		"""
		The helper function to start the traversal
		"""

		if node in self.visited:

			return

		#add the visited node 
		self.visited.add(node)

		#print the node
		print(node)

		#traverse the node
		for neighbor in self.graph[node] :

			self.dfs_helper(neighbor)



	def bfs_traversal(self, node) :
		"""
		The function to start the bfs traversal
		"""

		#make the queue
		queue = deque()

		#visisted set
		visited = set(node)

		#add the node to queue
		queue.append(node)

		#start the traversal 
		while queue :

			#pop the node 
			curr_node = queue.popleft()

			#print the node
			print(curr_node)

			#traverse the nodes
			for neighbor in self.graph[curr_node] :

				#check the neighbor in visited
				if neighbor in visited :

					continue 

				#put the neigbor in visited
				visited.add(neighbor)

				#add to the queue
				queue.append(neighbor)






class GridHelper():

	def __init__(self):

		self.grid = [
		["1","1","1","1","0"],
		["1","1","0","1","0"],
		["1","1","0","0","0"],
		["0","0","0","0","0"]
		]

		self.visited = set()


	def dfs_helper(self,  x , y) :


		directions = [
		(1, 0),
		(-1, 0),
		(0, 1),
		(0, -1)
		]

		#condition limits
		if x < 0 or x >= self.rows or y < 0 or y >= self.cols:
			
			return

		#if visited
		if self.grid[x][y] == "#":

			return


		# Already visited
		if (x, y) in self.visited:
			
			return

		#print the val
		print(self.grid[x][y])
		
		# Mark visited
		self.visited.add((x, y))


		#traverse the dirs
		for dir_x , dir_y in directions :

			self.dfs_helper( dir_x + x , dir_y + y )



	def dfs_traversal(self) :
		"""
		the dfs traversal for the grid graph
		"""
		#make the row and col length
		self.rows = len(self.grid)
		self.cols = len(self.grid[0])

		for x in range(self.rows) :

			for y in range(self.cols) :

				self.dfs_helper(x , y )







#call the main function 

if __name__ == "__main__" :

	tree_helper = TreeHelper()

	dfs_res = tree_helper.dfs_traversal(first)

	print(dfs_res)

	bfs_res = tree_helper.bfs_traversal(first) 

	print(bfs_res)

	adjacenylistgraph = AdjacenyListGraph()

	dfs_traversal_adjacency_list = adjacenylistgraph.dfs_traversal()

	print(dfs_traversal_adjacency_list)

	gridhelper = GridHelper()

	dfs_traversal_grid = gridhelper.dfs_traversal()

	print(dfs_traversal_grid)

































