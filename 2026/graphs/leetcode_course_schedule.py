"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
"""

"""
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.


"""


"""
The approach is to check for the cycle in the graph is cycle is detected we can't do the course 
traverse the graph in dfs or bfs and then find cycle
we can store the points and find the cycle

do we need to make a graph like list 

mapper = {0 : [1,0] , 1 : [1,0] } 




"""





from typing import List
from collections import defaultdict




class SolutionWrong:
	def __init__(self):

		self.graph = {}
		self.visited = set()
		


	def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
		"""
		The function to find the course that can be finish
		"""

		#make the graph
		self._make_graph( prerequisites )

		#travese the graph
		for node in self.graph :

			self._dfs_helper(node)

		


	def _make_graph(self,prerequisites) :
		"""
		The function to make the graph
		"""

		i = 0

		for edge in prerequisites :

			adj_list = []

			for node in edge : 

				adj_list.append(node)

			self.graph[i] = adj_list

			i += 1

		return self.graph


	def _dfs_helper(self, node):
		"""
		The dfs helper function to travers the graph
		"""

		self.visited.add(node)

		for neighbor in self.graph[node] :

			if neighbor not in self.visited :

				self._dfs_helper(neighbor)





if __name__ == "__main__" :

	sol = SolutionWrong()

	prerequisites = [[1,0],[0,1]]

	numCourses = 2 

	sol.canFinish( numCourses , prerequisites )











class Solution():


	def __init__(self):

		self.visited = set()
		self.graph = defaultdict(list)
		self.path = set()


	def _make_graph(self,prerequisites) :
		"""
		The function to make the graph
		"""

		for u,v in prerequisites :


			self.graph[u].append(v)



	def _check_cycle(self, node) :
		"""
		The functtion to traverse the graph in dfs
		"""

		#check the node 
		if node in self.visited :

			return False

		#if node found in path
		if node in self.path :

			return True


		#add the node in the path
		self.path.add(node)

		#travese the graph

		for neighbor in self.graph[node] :

			if self._check_cycle(neighbor) :

				return True

		#remove the node
		self.path.remove(node)

		#mark the visited node
		self.visited.add(node)

		return False





	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		"""
		The function to find the course can be done
		"""

		#base case 
		if len(prerequisites) == 1 :

			return True


		#make the graph 
		self._make_graph(prerequisites)

		#travserse the graph
		for course in range(numCourses) :

			if course not in self.visited :

				if self._check_cycle(course) :

					return False


		return True









if __name__ == "__main__" :

	sol = Solution()

	numCourses = 2 

	prerequisites = [[1,0],[0,1]]

	res = sol.canFinish( numCourses , prerequisites)

	print(res)













































































