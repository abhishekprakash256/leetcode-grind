"""
find the valid tree 

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges 

where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""


"""
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

"""


"""
approach -- 

using dfs and recursive stack 

track the ndoe and return the response 

"""

from collections import defaultdict


class Solution_wrong():

    def __init__(self):

        self.visited = set()
        self.recusive_stack = set()
        self.graph = defaultdict(list)

    def make_graph(self, edges) :
        """
        The function to make the graph 
        """

        #make the graph by iteration
        for a , b in edges :

            self.graph[a].append(b)

    def helper_dfs(self,node):
        """
        The function to iterate the dfs in the graph
        """

        #base case
        
        #if found in recursive stack
        if node in self.recusive_stack :

            return True

        #node found in visted
        if node in self.visited :

            return False

        #add the node 
        self.visited.add(node)

        self.recusive_stack.add(node)

        #make the recusive call
        for neighbor in self.graph[node] :

            if self.helper_dfs(neighbor) :

                return True

        #remove the node
        self.recusive_stack.remove(node)

        return False

    def validTree(self, n, edges) -> bool:
        """
        The function to check if the tree is valid
        """
 
        self.n = n 

        #constraints case 

        #not have edge 
        if self.n == 0 :

            return False

        if self.n == 1 :

            return True

        #make the graph
        self.make_graph(edges)

        #make the recursive calls
        for i in range(self.n):

            if self.helper_dfs(i) :

                return False

        return True



class Solution_one:
    """
    passes leetcode
    """
    def __init__(self):
        self.visited = set()
        self.graph = defaultdict(list)

    def make_graph(self, edges):
        """Build adjacency list."""
        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)  # Undirected graph

    def helper_dfs(self, node, parent):
        """DFS to detect cycle and check connectivity."""
        self.visited.add(node)

        for neighbor in self.graph[node]:
            if neighbor == parent:  
                continue  # Ignore the edge leading back to the parent

            if neighbor in self.visited:
                return True  # Cycle detected
            
            if self.helper_dfs(neighbor, node):
                return True  # Propagate cycle detection

        return False

    def validTree(self, n, edges):
        """Check if the given graph is a valid tree."""
        if len(edges) != n - 1:
            return False  # A tree must have exactly (n - 1) edges

        self.make_graph(edges)

        # Start DFS from node 0
        if self.helper_dfs(0, -1):  
            return False  # Cycle detected

        # Check if all nodes were visited (Graph must be fully connected)
        return len(self.visited) == n





class Solution_two:
    """
    passes leetcode 
    """
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
        self.recursion_stack = set()  # This will track the current path

    def make_graph(self, edges):
        # Build the graph from the edges
        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)  # Undirected graph

    def dfs(self, node, parent):
        # If the node is already in the recursion stack, it means we have found a cycle
        if node in self.recursion_stack:
            return True

        # If the node is already visited, no need to explore it again
        if node in self.visited:
            return False

        # Mark the node as visited and add it to the recursion stack
        self.visited.add(node)
        self.recursion_stack.add(node)

        # Explore all neighbors of the current node
        for neighbor in self.graph[node]:
            # If a cycle is detected in the neighbor, return True
            if neighbor != parent and self.dfs(neighbor, node):
                return True

        # Remove the node from the recursion stack after exploring all neighbors
        self.recursion_stack.remove(node)
        return False

    def validTree(self, n, edges):
        # Edge case: If there are no edges but more than one node, it's not a valid tree
        if n - 1 != len(edges):
            return False

        # Make the graph
        self.make_graph(edges)

        # Start DFS from node 0
        # If DFS detects a cycle, return False
        if self.dfs(0, -1):
            return False

        # Ensure all nodes were visited (the graph should be connected)
        return len(self.visited) == n






class Solution():
    """
    passes leetcoode
    """

    def __init__(self):

        self.graph = defaultdict(list)
        self.visited = set()
        self.recursion_stack = set()

    def make_graph(self,edges):
        """
        The function to make the graph
        """

        for a,b in edges :

            #append the edges in dict and make graph
            self.graph[a].append(b)
            self.graph[b].append(a)



    def helper_dfs(self,node, parent):
        """
        The heleper dfs function to find the graph is a tree or not 
        """

        #base case 

        #if in the rec stack 
        if node in self.recursion_stack :

            return True

        if node in self.visited :

            return False

        #add the node in the visied and rec stack 
        self.visited.add(node)
        self.recursion_stack.add(node)

        #iterate over the neighbor
        for neighbor in self.graph[node] :

            if neighbor != parent and self.helper_dfs(neighbor,node) :

                return True

        #remove the node 
        self.recursion_stack.remove(node)

        return False




    def validTree(self, n, edges):
        """
        The function to find if a tree is valid or not
        """

        #constraints case 

        #no edge
        if n - 1 != len(edges):
            return False


        #make the graph
        self.make_graph(edges)

        #make the vars 
        start_node = 0
        parent = -1 

        #make the recursive traversal 
        if self.helper_dfs(start_node, parent) :

            return False

        return len(self.visited) == n





























