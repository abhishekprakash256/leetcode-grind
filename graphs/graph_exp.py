"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

 

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
start with making graph


[[1,2],[2,3],[3,4],[1,4]]


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


#make graph 


from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Graph_Helper():

    def make_graph(self,adj_list):
        """
        function to make the graph
        """

        nodes = {}

        for u,v in adj_list :

            if u not in nodes :

                nodes[u] = Node(u)

            if v not in nodes :

                nodes[v] = Node(v)

            nodes[u].neighbors.append(nodes[v])

        #return the smaller or any node 
        return nodes[min(nodes.keys())]



    def traverse_graph_dfs(self,node, visited = None):
        """
        The function to traverse the graph
        """

        #base
        if not node:

            return

        if visited is None:

            visited = set()

        if node.val in visited :

            return

        visited.add(node.val)
        print(node.val)


        for neighbour in node.neighbors :

            self.traverse_graph_dfs(neighbour , visited)












def dfs_recursive(node, graph, visited=None, results=None):
    """
    The function to make the recursive dfs calls for tree 
    """

    #base case 
    if visited is None :

        visited = set()

    if results is None:
        results = []

    if node in visited:
        
        return 

    #add the node
    visited.add(node)
    results.append(node)

    #make the recursion
    for neighbor in graph[node] :

        if neighbor not in visited :

            dfs_recursive(neighbor, graph, visited, results)

    return results





def dfs_stack(node,graph):
    """
    The function to do the dfs traversal in the graph 
    """

    #make the visited 
    visited = set()

    #make the results 
    results = []

    #make the stack
    stack = [node]

    #traversal for the graph
    while stack :

        temp_node = stack.pop()

        if temp_node not in visited :

            results.append(temp_node)
            visited.add(temp_node)

            for neighbor in graph[temp_node] :

                if neighbor not in visited :

                    stack.append(neighbor)

    return results






def bfs_graph(node,graph) :
    """
    The function to traverse the graph the in bfs
    """

    visited = set()

    queue = deque([node])

    results = []

    #iter the graph 

    while queue :

        temp_node = queue.popleft()

        if temp_node not in visited :

            results.append(temp_node)
            visited.add(temp_node)

            for neighbor in graph[temp_node] :

                if neighbor not in visited :

                    queue.append(neighbor)

    return results




def dfs_cycle(node, graph, visited=None, path=None):
    """
    Detects cycle in a directed graph using DFS.
    Returns True if a cycle is found.
    """

    if visited is None:

        visited = set()

    if path is None:

        path = set()

    if node in path:

        return True  # cycle found

    if node in visited:
        
        return False  # already processed safely

    #add to path
    path.add(node)

    for neighbor in graph[node]:
        if dfs_cycle(neighbor, graph, visited, path):
            return True

    path.remove(node)
    visited.add(node)

    return False

















adj_list = [[1,2],[2,3],[3,4],[4,1]]

graph_helper = Graph_Helper()

#graph_node = graph_helper.make_graph(adj_list)

#graph_helper.traverse_graph_dfs(graph_node)



graph = {
    1: [2],
    2: [3],
    3: [4],
    4: [1]  # forms a cycle
}




print(dfs_recursive(1, graph))

print(dfs_stack(1,graph ))

print(bfs_graph(1,graph))


for node in graph:
    if dfs_cycle(node, graph ):
        print("Cycle detected")
        break
else:
    print("No cycle")














































