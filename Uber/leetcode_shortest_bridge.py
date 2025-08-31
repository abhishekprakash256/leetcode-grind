"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. 
There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.
"""

"""

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:

	n == grid.length == grid[i].length
	2 <= n <= 100
	grid[i][j] is either 0 or 1.
	There are exactly two islands in grid.



"""

"""


The grid is the connection of the 1's that connect to each other vertically or horniontally 

1 Find the islands 
2. Find the bridge 

1. Find the island  - 

- find the 1 and make bfs search on the traversal to identify the islnd 
move the up and down and can make an island we can keep the count of the 1's 


first find the one of the island then go to the last -- 

when the chnage of the number comes look for another 1 and explore to find the shgortest path using bfs 

we can find the island and exhaust the last points all end coordiantes 

find the other island and store the cooreduinates 

start the search from the end to other end using BFS 


sudo code 

first_islnad_edge = []
second_island_edge = [] 


def dfs(i,j,edge_lst):

	all edge cond 
	
	if 






count = 0 

for i in range row:

	for j in range col :

		if matix[i][j] == 1 :

			first_island_edges.append([i,j])
			self.dfs(i,j , first_island_edges)

			count += 1 




"""

from typing import List
from collections import deque



class Solution_wrong:

	def dfs(self,i,j):
		"""
		The method to find the complete island
		"""

		#constraint condn
		if i < 0 or i >= self.row or j < 0 or j >= self.col or self.grid[i][j] == 0:
			
			return

		#make the point as 2
		self.grid[i][j] = 2

		#move into the dirs
		self.dfs(i-1,j)
		self.dfs(i+1,j)
		self.dfs(i,j+1)
		self.dfs(i,j-1)



	def shortestBridge(self, grid: List[List[int]]) -> int:
		"""
		The function to find the shortest bridge
		"""

		self.grid = grid
		self.row = len(self.grid)
		self.col = len(self.grid[0])

		#the queue for bfs
		queue = deque()

		#directiosn to move
		dirs = [[0,1],[0,-1],[-1,0],[1,0]]

		#the visited dict
		visited = {}

		#distance 
		dist = 0


		#iter and find the first one 
		for i in range(self.row) :

			for j in range(self.col):

				#find the grid value 1
				if self.grid[i][j] == 1 :

					#pass into the dfs
					self.dfs(i,j)

					queue.append([i,j])

					break

		#find the shortest distance
		while queue :

			#pop from the queue
			x , y = queue.popleft()

			#move in the dirs
			for dir_x, dir_y in dirs :

				nx = x + dir_x
				ny = y + dir_y

				#catch the visited
				if (nx,ny) not in visited or self.grid[nx][ny] != 2 or x >= 0 or x <= self.row or ny >= 0 or ny <= self.col :

					queue.append([nx,ny])

					visited[(nx,ny)] = True

					dist += 1

					print(nx,ny)

					if self.grid[nx][ny] == 1 :

						return dist



class Solution():


	def dfs(self,i,j):
		"""
		The method to do the dfs for the grid
		"""

		#the constraint case 
		if i < 0 or i >= self.row or j < 0 or j >= self.col or self.grid[i][j] != 1 :

			return

		#mark the grid as 2
		self.grid[i][j] = 2

		#add in the queue 
		self.queue.append([i,j])

		#iter the grid
		self.dfs(i-1,j)
		self.dfs(i+1,j)
		self.dfs(i,j-1)
		self.dfs(i,j+1)





	def shortestBridge(self, grid: List[List[int]]) -> int:
		"""
		The function to find the shortest bridge
		"""

		self.grid = grid

		#get the dims 
		self.row = len(self.grid)
		self.col = len(self.grid[0])

		self.queue = deque()

		visited = {}

		found = False

		dirs = [[0,1],[0,-1],[-1,0],[1,0]]

		dist = 0

		#find the 1 in the grid
		for i in range(self.row) :

				for j in range(self.col) :

					if self.grid[i][j] == 1 :

						self.dfs(i,j)

						found = True

						break

				if found :

					break


		#start the bfs for the traversal
		while self.queue :


			for _ in range(len(self.queue)) :

				x , y = self.queue.popleft()

				for dir_x , dir_y in dirs :

					_x , _y = x + dir_x , y + dir_y

					if 0 <= _x < self.row and 0 <= _y < self.col and (_x,_y) not in visited:

						if self.grid[_x][_y] == 0:

							self.queue.append([_x,_y])

							visited[(_x,_y)] = True

						elif self.grid[_x][_y] == 1:

							return dist

				dist += 1 



























if __name__ == "__main__":

	sol = Solution()

	grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

	res = sol.shortestBridge(grid)

	print(res)







		
		




















































