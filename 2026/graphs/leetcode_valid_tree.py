"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is 

an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""



"""
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

Output: true


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.


"""


"""
approach -- 

- use the cycle detection , to find the tree 
- make the graph , find the cycle , if cycle found return false 
- if cycle not found return False



"""

from typing import List
from collections import defaultdict



class Solution:
	def __init__(self):

		self.graph = defaultdict(list)
		self.path = set()
		self.visited = set()

	def _make_graph(self, edges: list[list[int]]) :
		"""
		The function to make the graph
		"""

		#iter the list
		for u,v in edges :

			self.graph[u].append(v)


	def _check_cycle(self, node ) :
		"""
		The function to traverse the dfs graph 
		"""

		#check the node 
		if node in self.visited :

			return False

		#if node found in path
		if node in self.path :

			return True

		#add the node in the path
		self.path.add(node)


		#traserse the node
		for neighbor in self.graph[node] :

			if self._check_cycle(neighbor) :

				return True

		#remove the node
		self.path.remove(node)

		#mark the visited node
		self.visited.add(node)

		return False






	def validTree(self, n: int, edges: list[list[int]]) -> bool:
		"""
		Find the valid tree
		"""

		#base case 
		if n == 1 :

			return True


		#make the graph 
		self._make_graph(edges)

		#travserse the graph
		for course in range(n) :

			if course not in self.visited :

				if self._check_cycle(course) :

					return False


		return True







#the main block
if __name__ == '__main__':

	sol = Solution()

	edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

	n = 5

	res = sol.validTree( n , edges)

	print(res)