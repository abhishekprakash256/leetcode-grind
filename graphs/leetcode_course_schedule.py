"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

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
approach -- 


make the graph 

it's a unidirected graph 

detect the cycle using the path

"""
from collections import defaultdict


class Solution:
    """
    passes leet code 
    """

    def __init__(self):

        self.visited = set()
        self.graph = defaultdict(list)
        self.path = set()

    def _make_graph(self):
        """
        The function to make the graph
        """

        #travers the graph
        for u,v in self.prerequisites :

            self.graph[u].append(v)
            

    def _check_cycle(self,node):
        """
        The function to check the cycle in graph
        """ 

        #base case 
        if node in self.visited :

            return False

        if node in self.path :

            return True

        #add the node 
        self.path.add(node)

        for neighbor in self.graph[node] :

            if self._check_cycle(neighbor) :

                return True

        self.path.remove(node)

        self.visited.add(node)

        return False



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        The function to check the course can be done
        """

        #constraint case 
        if len(prerequisites) == 1 :

            return True

        self.prerequisites = prerequisites

        #make graph 
        self._make_graph()

        #check the graph for cycle

        for coures in range(numCourses) :

            if coures not in self.visited :

                if self._check_cycle(coures) :

                    return False

        return True


