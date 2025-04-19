"""
Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

"""


"""
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.


"""



"""
approach -- 

make a dict of the graph like, 

make a node and traverse 

make a deep copy using the graph



"""

from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution():

    self.mapper = defaultdict(list)
    self.copy_mapper = {}


    def _make_graph(self,adj_list):
        """
        The function to make the graph 
        """

        #iter the list
        for u,v in adj_list :

            self.mapper[u].append(v)
            self.mapper[v].append(u)

    def _make_node_copy(self):
        """
        The function to make to node copy
        """

        #iter the graph

        for u in self.mapper :

            node = Node(self.mapper[u])

            self.copy_mapper[u] = node


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        The function to clone the graph
        """

        #make the graph
        self._make_graph()

        #make the clone graph

        for copy_node in self.copy_mapper :

            self.copy_mapper[copy_node].neighbors.append()




























