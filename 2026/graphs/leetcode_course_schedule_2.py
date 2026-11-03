"""

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""


"""
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]



Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.



"""



"""

approach --- 

make the graph , then traverse the graph using the dfs and find how we can make the course affective

how can I get the order ?? 

we can add into a list and get the values into it 

"""


from typing import List
from collections import defaultdict


class Solution:

	def __init__(self):

		self.visited = set()
		self.graph = defaultdict(list)
		self.path = set()
		self.course_path = []


	def _make_graph(self , prerequisites: list[list[int]]):
		"""
		The function to make the graph
		"""

		for u,v in prerequisites :


			self.graph[u].append(v)


	def _check_cycle(self, node):
		"""
		The function to traverse the graph
		"""

		#check the node is viisted 
		if node in self.visited :

			return False

		#if node found in path
		if node in self.path :

			return True


		#add the node in the path
		self.path.add(node)


		#travers the node 
		for neighbor in self.graph[node] :

			if self._check_cycle(neighbor) :

				self.course_path.append(neighbor)

				return True

		#remove from the path 
		self.path.remove(node)

		#add to the path
		self.visited.add(node)

		return False




	def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
		"""
		The function to find the course that can be taken
		"""
		
		#make the graph 
		self._make_graph(prerequisites) 


		#travsese the graph 
		for course in range(numCourses) :

			if course not in self.visited :

				if self._check_cycle(course) :

					return False

		return self.course_path





if __name__ == "__main__" :

	sol = Solution()

	numCourses = 2 

	prerequisites = [[1,0],[0,1]]

	res = sol.findOrder( numCourses , prerequisites)

	print(res)


			
		

