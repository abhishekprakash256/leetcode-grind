"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

"""

"""
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So the correct course order is [0,1].


Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

"""



"""
approach -- 

the order we take the course -- ? 


make the graph same way using dafultdict with list

from collections import defaultdict

self.graph = defaultdict(list)  # Store graph as adjacency list

def make_graph(self, prerequisites):

    for a, b in prerequisites:
        self.graph[a].append(b)  # Directed edge: a -> b


check cycle as well 

if true , return order ? 

direted graph ? 

return path from 0 to last

dfs can find path or bfs ? 

find any path ?

dfs how I know the last node is reached ? 

n-1 is the last node and start is from 0 

that can be the base case 

"""

from collections import defaultdict


class Solution_wrong():

    def __init__(self):

        self.visited = set()
        self.recusive_stack = set()
        self.graph = defaultdict(list)


    def make_graph(self, prerequisites):
        """
        The funciton to make the graph 
        """
        
        #iterate the list
        for a,b in prerequisites :

            self.graph[a].append(b) #make the graph


    def helper_dfs(self,node, result) :
        """
        The helper function to find the path and check for cycle 
        """

        #base case

        #if node in recursive stack
        if node in self.recusive_stack :

            return []

        if node in self.visited :

            return result

        #add the node 
        self.visited.add(node)

        #add the node in stack
        self.recusive_stack.add(node)

        print("inside the fun",result)

        #make the recursive calls
        for neighbor in self.graph[node] :

            path = self.helper_dfs(neighbor , result + [neighbor] )

            if path :

                return path

        #flush the node from stack 
        self.recusive_stack.remove(node)

        return result



    def findOrder(self,numCourses , prerequisites) :
        """
        The function to find the order of the visit
        """

        self.numCourses = numCourses
        
        #constarints case 

        #only one node 
        if numCourses == 1 :

            return [0]

        #make graph 
        self.make_graph(prerequisites)

        print(self.graph)

        #result list
        result = []

        #make the recusive dfs call 
        for node in range(numCourses):  # Check all nodes (0 to numCourses-1)

            print(node)

            if node not in self.visited :

                path = self.helper_dfs(node, result + [node])

                if path :
                    return path

        return []




















#test case 
numCourses = 4 
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

sol = Solution()

print(sol.findOrder(numCourses, prerequisites))
















