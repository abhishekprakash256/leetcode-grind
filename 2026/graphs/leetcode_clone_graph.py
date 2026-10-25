"""
For simplicity, each node's value is the same as the node's index (1-indexed). 

For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. 

Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. 

You must return the copy of the given node as a reference to the cloned graph.
"""

"""

make a dummy node , then traverse the graph using the dfs or bfs and then add the node 
return the node.next ?? 



"""


# Definition for a Node.
class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:

	def __init__(self) :

		self.mapper = {}


	def _dfs_helper(self, node ):
		"""
		The function to traverse the graph
		"""

		#if the node is found
		if node in self.mapper :

			return self.mapper[node]

		#make the clone node
		clone = Node(node.val)
		self.mapper[node] = clone

		#maek the neighbors 
		for neighbor in node.neighbors :

			clone.neighbors.append(self._dfs_helper(neighbor))

		return clone



	def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
		"""
		The function to clone the graph
		"""

		#if the node is empty
		if not node:

			return None

		return self._dfs_helper(node)






