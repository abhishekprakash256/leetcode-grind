"""
You have a graph of n nodes. You are given an integer n and an array edges where 
edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

"""

"""
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.

"""

"""
approach -- 

first make the graph in both ways 

make a traversal and mark the node 

count the node from start

if enounter a node return 1 

dfs traversal and mark the way (original temp ? )

"""
from collections import defaultdict


class Solution():
    """
    passes leetcode
    """

    def __init__(self):

        self.graph = defaultdict(list)

        self.visited = set()


    def make_graph(self,edges):
        """
        The function to make the graph
        """

        for a, b in edges :

            self.graph[a].append(b)
            self.graph[b].append(a)


    def helper_dfs(self,node):
        """
        The function to make the helper dfs
        """
        #base case 

        if node in self.visited :
            
            return

        #print the node 
        #print(node)

        #add in the visited 
        self.visited.add(node)

        for neighbor in self.graph[node]:

            self.helper_dfs(neighbor)
        


    def countComponents(self, n , edges) :
        """
        The function to count the number of connected edges 
        """

        #constraints case 

        #if one node 
        if n == 1 :

            return 1

        #make the graph
        self.make_graph(edges)

        #print(self.graph)

        #count vars 
        count = 0 

        #do the recursive traversal 
        for node in range(n) :

            if node not in self.visited :

                count +=1 

                self.helper_dfs(node)

        return count





class Solution():

    def __init__(self):

        self.graph = defaultdict(list)
        self.visited = set()
        self.count += 1 


    def _make_graph(self,edges):
        """
        The function to make the graph by edges list
        """

        for u,v in edges :

            self.graph[u].append(v)
            self.graph[v].append(u)


    def _helper_dfs(self,node):
        """
        The function to traverese the graph in dfs 
        """

        #base case
        if node in self.visited :

            return

        #add the node
        self.visited.add(node)

        #travere the graph
        for neighbor in self.graph[node] :

            if neighbor not in self.visited :

                self._helper_dfs(neighbor)



    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        The function to find the number of number of connected components
        """

        #constraint case 

        if n == 1 :

            return 1

        #make the graph
        self._make_graph(edges)

        #traverese the graph
        for node in range(n):

            if node not in self.visited :

                self._helper_dfs(node)
                self.count += 1 

        #return the count
        return self.count






































































n = 5

edges = [[0,1],[1,2],[2,3],[3,4]]

sol = Solution()

print(sol.countComponents(n ,edges))




