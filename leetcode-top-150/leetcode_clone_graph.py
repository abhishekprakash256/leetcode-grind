"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.
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

"""


"""
approach - 

dfs make a node and traverse and add neighbors 
base case 
if not node:
	return []

if node.neighbors is None:
	return [[]]


class Solution:
	def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


queue = [node]

visisted = set()


while queue:

	curr_node = queue.pop(0)

	temp_node = Node(node.val)

	if curr_node.val not in visited:

		temp_node = Node(node.val)

		for neighbors in curr_node.neighbors:

			queue.append(neigbors)

			temp_node.neighbors = Node(neighbors.val)


"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution2:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clones a graph using BFS.
        """
        if not node:
            return None
        
        # A mapping from original node to its clone
        clone_map = {}

        # Initialize the queue with the original node
        queue = [node]
        
        # Clone the first node and add it to the map
        clone_map[node] = Node(node.val)

        while queue:
            # Pop the current node from the queue
            curr_node = queue.pop(0)
            
            # Traverse all its neighbors
            for neighbor in curr_node.neighbors:
                if neighbor not in clone_map:
                    # Clone the neighbor and add it to the map
                    clone_map[neighbor] = Node(neighbor.val)
                    # Add the original neighbor to the queue
                    queue.append(neighbor)
                
                # Link the current node's clone to the neighbor's clone
                clone_map[curr_node].neighbors.append(clone_map[neighbor])
        
        # Return the clone of the input node
        return clone_map[node]








class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            # Clone the current node
            clone = Node(node.val)
            visited[node] = clone

            # Clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

