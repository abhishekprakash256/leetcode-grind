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
do I need to make a graph first ??? 


traverse the graph and find cycle connections ??

one cycle is one proivince 

when the connection disconnects , how to find the island ?? 

so this question can be solved like island problem , traves the one and then mark that then other make and increse the count

whenever we traverse the graph, mark 
"""

from typing import List

class Solution():

	def __init__(self):

		self.adj_list = {}
		self.count = 0 
		self.visited = set()

	def _make_graph(self , isConnected : List[List[int]] ) :
		"""
		The function to make the graph
		"""

		for i in range(len(isConnected) ) :

			self.adj_list[i] = []

			for j in range(len(isConnected[i])) :

				if isConnected[i][j] == 1 :

					self.adj_list[i].append(j)


		return self.adj_list


	def findCircleNum(self, isConnected: List[List[int]]) :
		"""
		The function to find the number of the provinces
		""" 

		#make the graph
		self._make_graph(isConnected)

		#make dfs search
		for node in range(len(isConnected)):

			if node in self.visited:

				continue

			self.count += 1

			self._dfs_helper(node)

		return self.count





	def _dfs_helper(self, node) :
		"""
		The function to traverse the graph
		"""
		#print(node)

		self.visited.add(node)

		#print(node)

		for neighbor in self.adj_list[node] :

			if neighbor in self.visited :

				continue

			self._dfs_helper(neighbor)








if __name__ == "__main__" :

	sol = Solution()

	isConnectedTwo = [[1,0,0],[0,1,0],[0,0,1]]  # 3 

	isConnected = [[1,1,0],[1,1,0],[0,0,1]]   #2

	res = sol.findCircleNum( isConnected )

	#print(sol.adj_list)

	print(res)












