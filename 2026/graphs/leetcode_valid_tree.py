"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is 

an undirected edge between nodes ai and bi in the graph.

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

- this is an undirected graph
- graph will be made using u and v 
- we need to track the parent and key idea is node != parent, duing the dfs traversal



"""
from typing import List
from collections import defaultdict


class Solution:

    def __init__(self):

        self.graph = defaultdict(list)
        self.visited = set()


    def _make_graph(self, edges):

        for u, v in edges:

            self.graph[u].append(v)
            self.graph[v].append(u)


    def _check_cycle(self, node, parent):

        self.visited.add(node)

        for neighbor in self.graph[node]:

            if neighbor == parent:
                continue

            if neighbor in self.visited:
                return False

            if not self._check_cycle(neighbor, node):
                return False

        return True


    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # A tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        self._make_graph(edges)

        # Check cycles and connectivity
        if not self._check_cycle(0, -1):
            return False

        return len(self.visited) == n