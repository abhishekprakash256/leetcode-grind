"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

	For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.


"""

"""

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.


Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.




"""

"""

aapproach -- 

using the traversal find the cycle 

not a graph 

no neighbors ? 



"""


#make graph testing 

numCourses = 4
prerequisites0 = [[0, 1], [1, 2]]

"""
graph = {
	1: [0],  # Course 1 points to course 0
	2: [1]   # Course 2 points to course 1
}
"""


prerequisites1 = [[1, 0], [2, 1], [3, 2]]

#out {0: [1], 1: [2], 2: [3]}


prerequisites = [[0, 1], [1, 2], [2, 0], [3, 2]]

"""
graph = {
	1: [0],
	2: [1, 3],
	0: [2]
}
"""



def make_graph(prerequisites) : 
	"""
	The function to make the graph 
	"""

	graph = {}

	for edge in prerequisites : 

		edge.reverse()

		if edge[0] not in graph:

			graph[edge[0]] = []

		for i in range(1,len(edge)):

			graph[edge[0]].append(edge[i])

	return graph




class Solution1:

	def __init__(self):

		self.graph = {}
		self.visited = {}
		self.recursion_stack = {}


	def make_graph(self,prerequisites):
		"""
		The function to make graph
		"""

		for edge in prerequisites:

			edge.reverse()	

			if edge[0] not in self.graph:

				self.graph[edge[0]] = []

			for i in range(1,len(edge)):

				self.graph[edge[0]].append(edge[i])



	def dfs_graph(self, node):
		"""
		DFS traversal to detect cycles in the graph.
		"""
		if node in self.recursion_stack:
			# Cycle detected
			return True
		if node in self.visited:
			# Node already processed
			return False

		# Mark the node as visited and add to recursion stack
		self.visited[node] = True
		self.recursion_stack[node] = True

		# Traverse neighbors
		for neighbor in self.graph.get(node, []):
			if self.dfs_graph(neighbor):  # Cycle found in the subgraph
				return True



	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		"""
		The function to fid the couse schedule 
		try to find cycle in graph 

		"""

		#base case 
		if not prerequisites:
			return None


		#make the graph 
		self.make_graph(prerequisites)

		for node in range(numCourses):
			if node not in self.visited:
				if self.dfs_graph(node):  # If a cycle is detected
					return False

		return True


		













#example graph 

"""
graph = {
	1: [0],
	2: [1, 3],
	0: [2]
}
"""


		
class Solution():
	"""
	Works in leetcode

	"""

	def __init__(self):

		self.graph = {}
		self.visited = {}
		self.recursion_stack = {}

	
	def make_graph(self,prerequisites):
		"""
		The function to make graph
		"""

		for edge in prerequisites:

			edge.reverse()	

			if edge[0] not in self.graph:

				self.graph[edge[0]] = []

			for i in range(1,len(edge)):

				self.graph[edge[0]].append(edge[i])




	def dfs_traversal(self,node):
		"""
		The dfs traversal of the graph
		"""
		#cycle is detected
		if node in self.recursion_stack:
			return True

		#add the node in visited
		self.visited[node] = True

		#add the node in stack
		self.recursion_stack[node] = True

		#start the dfs traversal 
		if node in self.graph :

			for neighbor in self.graph[node] :

				if neighbor not in self.visited :

					if self.dfs_traversal(neighbor) :

						return True

				elif neighbor in self.recursion_stack :

					return True

		del self.recursion_stack[node]
		return False




	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		"""
		The function to do check the graph for cycle 
		"""
		#base case
		if len(prerequisites) == 1:
			return True


		if len(prerequisites) == 0 :
			return True


		#make the graph 
		self.make_graph(prerequisites)

		#traverse the the graph 
		for node in range(numCourses)

			if node not in self.visited :

				if self.dfs_traversal(node) :

					return False


		return True








































