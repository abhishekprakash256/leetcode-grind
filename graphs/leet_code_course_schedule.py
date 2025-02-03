"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

"""


#test cases 

numCourses = 2
prerequisites = [[1,0]]
out = True 


numCourses2 = 2 
prerequisites2 = [[1,0],[0,1]]
out2 = False

numCourses3 = 20 
prerequisites2 = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]


#not - correct solution -----

from collections import defaultdict

class Solution():

    def __init__(self):
        self.graph = defaultdict(list)  # Store graph as adjacency list
        self.visited = set()  # To track nodes already visited
        self.recursion_stack = set()  # To track nodes in the current DFS path

    def make_graph(self, prerequisites):
        """
        The function to build the graph from prerequisites
        """
        for a, b in prerequisites:
            self.graph[a].append(b)  # Directed edge: a -> b

    def helper_dfs(self, node):
        """
        Helper DFS function to detect a cycle in the graph
        """
        if node in self.recursion_stack:
            return True  # Found a cycle

        if node in self.visited:
            return False  # Already processed, no cycle here

        # Mark node as visited and part of the current DFS path (recursion stack)
        self.visited.add(node)
        self.recursion_stack.add(node)

        for neighbor in self.graph[node]:  # Iterate over all neighbors
            if self.helper_dfs(neighbor):  # If cycle is detected in any neighbor
                return True

        # After all neighbors are processed, remove from recursion stack
        self.recursion_stack.remove(node)
        return False  # No cycle found from this node

    def canFinish(self, numCourses: int, prerequisites) -> bool:
        """
        Determines if it's possible to finish all courses without a cycle
        """
        if len(prerequisites) == 0:
            return True  # No prerequisites, can finish all courses

        # Build the graph
        self.make_graph(prerequisites)

        # Check each course (node) for cycles using DFS
        for node in range(numCourses):  # Check all nodes (0 to numCourses-1)
            if node not in self.visited:  # If node not visited yet
                if self.helper_dfs(node):  # Detect cycle starting from node
                    return False  # Cycle found, cannot finish all courses

        return True  # No cycle detected, all courses can be finished





prerequisites2 = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]

sol = Solution()

print(sol.canFinish(20,prerequisites2))

print(sol.graph)




























if __name__ == '__main__':
    pass
    #sol =  Solution()
    #res = sol.canFinish(numCourses,prerequisites)


    #print(res)