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
- make the graph , find the cycle , 



"""

from typing import List
from collections import defaultdict



class Solution:
	def __init__(self):

		self.graph = defaultdict(list)
		self.path = set()
		self.visited = set()


	def _make_graph(self , edges : list[list[int]] ):
		"""
		The function to make the graph
		"""

		#mark the loop
		for u , v in edges :

			self.graph[u].append(v) 


	def _check_cycle(self , node):
		"""
		The function to check for the cycle
		"""

		#check in the visited
		if node in self.visited :

			return True

		#check the path
		if node in self.path :

			return False

		#add the node in the path
		self.path.add(node)


		#traverse in the node
		for neighbor in self.graph[node] :

			if self._check_cycle(neighbor) :

				return True

		#make the path
		self.path.remove(node)

		#mark the visited
		self.visited.add(node)

		return False



	def validTree(self, n: int, edges: list[list[int]]) -> bool:
		"""
		The function to find the valid tree
		"""

		#make the graph
		self._make_graph(edges)

		#traverse the graph
		for node in range(n) :

			if node not in self.visited :

				if self._check_cycle(node) :

					return False

		return True



