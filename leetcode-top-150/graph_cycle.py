"""
make the graph from scratech and detect cycles usid dfs 
"""

prerequisite1 = [[0, 1], [1, 2]]

"""
graph = {
	1: [0],  # Course 1 points to course 0
	2: [1]   # Course 2 points to course 1
}
"""


prerequisite2 = [[1, 0], [2, 1], [3, 2]]

#out {0: [1], 1: [2], 2: [3]}


prerequisite3 = [[0, 1], [1, 2], [2, 0], [3, 2]]

"""
graph = {
	1: [0],
	2: [1, 3],
	0: [2]
}
"""

class HelperFun():

	def __init__(self):

		self.visited = {}
		self.graph = {}
		self.res_lst = []

	def make_graph(self,prerequisites) : 
		"""
		The function to make the graph 
		"""

		self.graph = {}

		for edge in prerequisites : 

			edge.reverse()

			if edge[0] not in self.graph:

				self.graph[edge[0]] = []

			for i in range(1,len(edge)):

				self.graph[edge[0]].append(edge[i])

		return self.graph



	def dfs_graph(self, node):
		"""
		The DFS for the graph
		"""

		# If the node is already visited, return (skip it)
		if node in self.visited:
			return None

		# Mark the node as visited
		self.visited[node] = True

		# Traverse the neighbors of the node
		if node in self.graph:
			for neighbor in self.graph[node]:
				if neighbor not in self.visited:

					self.dfs_graph(neighbor)

		# Append the node to the result list after all its neighbors are visited (post-order)
		self.res_lst.append(node)


	def bfs_graph(self,node):
		"""
		The code for bfs traversal of the graph 
		"""

		#base case 
		if not node :
			return None 

		#make the visited
		visited = {}

		#make the queue
		queue = [node]

		#make the res list 
		res_lst = []

		while queue :

			curr_node = queue.pop(0)

			res_lst.append(curr_node)

			visited[curr_node] = True

			if curr_node in self.graph :

				for neighbor in self.graph[curr_node]:

					if neighbor not in self.visited:

						queue.append(neighbor)

		return res_lst







		


	def main(self):
		"""
		The function to run the dfs 
		"""

		first_node = list(self.graph.keys())[0]

		print(first_node)

		print(self.bfs_graph(first_node))


		#for the dfs 
		for node in self.graph:

			self.dfs_graph(node)

		return self.res_lst



if __name__ == "__main__":

	helper_fun = HelperFun()

	print(helper_fun.make_graph(prerequisite3))

	print(helper_fun.main())





