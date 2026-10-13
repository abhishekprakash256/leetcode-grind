"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""

"""


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

"""


"""

traverse the graph and find cycle connections ??

one cycle is one proivince 

when the connection disconnects , how to find the island ?? 

so this question can be solved like island problem , traves the one and then mark that then other make and increse the count

whenever we traverse the graph, mark 
"""

from typing import List

class Solution():

	def __init__(self):

		#self.graph = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

		self.visited = set()


	def findCircleNum(self , isConnected ):
		"""
		The function to traverse the graph using the adjaceny list
		"""

		node = isConnected[0][0]

		self.dfs_helper(node , isConnected )

	

	#make the helper traversal
	def dfs_helper(self, node , isConnected : List[List[int]]) :
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
		for neighbor in isConnected[node] :

			self.dfs_helper(neighbor , isConnected)



if __name__ == "__main__" :

	sol = Solution()

	isConnected = [[1,1,0],[1,1,0],[0,0,1]]

	res = sol.findCircleNum( isConnected )