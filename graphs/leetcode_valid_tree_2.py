"""
You have a graph of n nodes labeled from 0 to n - 1. 
You are given an integer n and a list of edges where edges[i] = [ai, bi] 
indicates that there is an undirected edge between nodes ai and bi in the graph.

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

make the graph 

use a visited
use a path 
make a graph
use the parent 



"""

from collections import defaultdict


class Solution():

	def __init__(self):

		self.graph = defaultdict(list)
		self.visited = set()
		self.path = set()

	def _make_graph(self,edges):
		"""
		The function to make the graph in dict form
		"""

		#iter the edges to make graph
		for u,v in edges :

			self.graph[u].append(v)
			self.graph[v].append(u)


	def _detect_cycle_dfs(self,node, parent):
		"""
		The function to check if the graph has cycle
		"""

		#base case 
		self.visited.add(node)

		#traverse the node
		for neighbor in self.graph[node] :

			if neighbor == parent :

				continue

			if neighbor in self.visited :

				return True

			if self._detect_cycle_dfs(neighbor , node):

				return True


		return False


	def validTree(self,n , edges ):
		"""
		The function to check the valid tree
		"""

		#constraint case 
		if n-1 != len(edges) :

			return False

		#make graph 
		self._make_graph(edges)

		#detect the cycle 
		if self._detect_cycle_dfs(0 , -1 ) :

			return False


		return len(self.visited) == n 

























