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


	def dfs_graph(self,node):
		"""
		The dfs for the graph
		"""
		
		if node in self.visited:
			return None

		#add the node in visited 
		self.visited[node] = True

		#traverse the nodes
		for neighbor in self.graph[node]:

			if neighbor not in self.graph:

				self.res_lst.append(neighbor)

				self.dfs_graph(neighbor)

		print(self.res_lst)





	def main(self):
		"""
		The function to run the dfs 
		"""

		for node in self.graph:

			self.dfs_graph(node)



if __name__ == "__main__":

	helper_fun = HelperFun()

	print(helper_fun.make_graph(prerequisite3))

	print(helper_fun.main())



